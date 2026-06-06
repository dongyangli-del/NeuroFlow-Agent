#!/usr/bin/env python3
"""Import a private Zotero BIB export into public Paper-RAG++ memory.

The script reads a BIB file from an ignored private path, removes private fields,
infers lightweight AI x neuroscience metadata, and writes public markdown maps.
It intentionally does not copy raw BIB entries, attachment paths, notes, or full
abstracts into public skill files.
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PAPER_RAG = ROOT / "skills" / "paper-rag-plus"
REFERENCES = PAPER_RAG / "references"
PRIVATE_ZOTERO = ROOT / ".private" / "zotero"
PRIVATE_REFERENCES = ROOT / ".private" / "references"

PRIVATE_FIELDS = {
    "file",
    "annote",
    "annotation",
    "note",
    "notes",
    "local-url",
}

UNVERIFIED = "Needs verification"
NOT_IDENTIFIED = "Not identified in imported metadata"
WEB_SOURCE = "OpenAlex public metadata"
MANUAL_CHECK = "待人工核验补充"


@dataclass
class Paper:
    key: str
    entry_type: str
    fields: dict[str, str]
    modalities: list[str] = field(default_factory=list)
    tasks: list[str] = field(default_factory=list)
    methods: list[str] = field(default_factory=list)
    datasets: list[str] = field(default_factory=list)
    domains: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    collections: list[str] = field(default_factory=list)
    web: dict[str, object] = field(default_factory=dict)

    @property
    def title(self) -> str:
        title = clean_tex(str(self.fields.get("title") or self.web.get("title") or UNVERIFIED))
        return title or UNVERIFIED

    @property
    def year(self) -> str:
        year = str(self.web.get("publication_year") or self.fields.get("year", UNVERIFIED))
        return clean_tex(year) or UNVERIFIED

    @property
    def venue(self) -> str:
        venue = (
            source_name(self.web)
            or self.fields.get("journal")
            or self.fields.get("booktitle")
            or self.fields.get("publisher")
            or infer_arxiv_venue(self.fields.get("note", ""), self.fields.get("url", ""))
        )
        return clean_tex(str(venue)) if venue else UNVERIFIED

    @property
    def doi(self) -> str:
        doi = self.web.get("doi") or self.fields.get("doi", UNVERIFIED)
        return clean_value(str(doi)).replace("https://doi.org/", "") or UNVERIFIED

    @property
    def authors(self) -> str:
        web_authors = authors_from_web(self.web)
        authors = web_authors or clean_tex(self.fields.get("author", UNVERIFIED))
        if authors == UNVERIFIED:
            return authors
        if web_authors:
            return authors
        parts = [part.strip() for part in re.split(r"\s+and\s+", authors) if part.strip()]
        if len(parts) > 8:
            return ", ".join(parts[:8]) + ", et al."
        return ", ".join(parts)

    @property
    def bib_type(self) -> str:
        return str(self.web.get("type") or self.entry_type or UNVERIFIED)


def clean_tex(value: str) -> str:
    value = clean_value(value)
    replacements = {
        r"\_": "_",
        r"\%": "%",
        r"\&": "&",
        "{": "",
        "}": "",
    }
    for src, dst in replacements.items():
        value = value.replace(src, dst)
    value = re.sub(r"\\[a-zA-Z]+\s*", "", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_value(value: str) -> str:
    value = value or ""
    value = value.replace("\n", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip().strip(",")


def source_name(web: dict[str, object]) -> str:
    primary = web.get("primary_location")
    if not isinstance(primary, dict):
        return ""
    source = primary.get("source")
    if not isinstance(source, dict):
        return ""
    return str(source.get("display_name") or "")


def authors_from_web(web: dict[str, object]) -> str:
    authorships = web.get("authorships")
    if not isinstance(authorships, list):
        return ""
    names = []
    for authorship in authorships[:8]:
        if not isinstance(authorship, dict):
            continue
        author = authorship.get("author")
        if isinstance(author, dict) and author.get("display_name"):
            names.append(str(author["display_name"]))
    if len(authorships) > 8:
        names.append("et al.")
    return ", ".join(names)


def strip_private_text(value: str) -> str:
    value = re.sub("/" + r"Users/[^,\s:})]+[^\s,})]*", "[private-path-removed]", value)
    value = re.sub("/" + r"home/[^,\s:})]+[^\s,})]*", "[private-path-removed]", value)
    value = re.sub("/" + r"vePFS-[^,\s:})]+[^\s,})]*", "[private-path-removed]", value)
    value = re.sub(r"[A-Za-z]:\\[^\s,})]+", "[private-path-removed]", value)
    return value


def parse_bib(text: str) -> list[Paper]:
    entries: list[Paper] = []
    i = 0
    while i < len(text):
        at = text.find("@", i)
        if at == -1:
            break
        brace = text.find("{", at)
        if brace == -1:
            break
        entry_type = text[at + 1 : brace].strip().lower()
        depth = 0
        end = brace
        for j in range(brace, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    end = j
                    break
        body = text[brace + 1 : end]
        if "," not in body:
            i = end + 1
            continue
        key, fields_text = body.split(",", 1)
        fields = parse_fields(fields_text)
        entries.append(Paper(key=key.strip(), entry_type=entry_type, fields=fields))
        i = end + 1
    return entries


def is_importable_reference(paper: Paper) -> bool:
    return any(
        clean_value(paper.fields.get(name, ""))
        for name in ("title", "doi", "abstract", "author")
    )


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    i = 0
    while i < len(text):
        while i < len(text) and (text[i].isspace() or text[i] == ","):
            i += 1
        name_start = i
        while i < len(text) and re.match(r"[A-Za-z0-9_\-]", text[i]):
            i += 1
        if i == name_start:
            i += 1
            continue
        name = text[name_start:i].strip().lower()
        while i < len(text) and text[i].isspace():
            i += 1
        if i >= len(text) or text[i] != "=":
            continue
        i += 1
        while i < len(text) and text[i].isspace():
            i += 1
        value, i = parse_value(text, i)
        if name not in PRIVATE_FIELDS:
            fields[name] = strip_private_text(value)
    return fields


def parse_value(text: str, i: int) -> tuple[str, int]:
    if i >= len(text):
        return "", i
    if text[i] == "{":
        depth = 0
        start = i + 1
        for j in range(i, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    return text[start:j], j + 1
    if text[i] == '"':
        start = i + 1
        escaped = False
        for j in range(i + 1, len(text)):
            if text[j] == "\\" and not escaped:
                escaped = True
                continue
            if text[j] == '"' and not escaped:
                return text[start:j], j + 1
            escaped = False
    start = i
    while i < len(text) and text[i] != ",":
        i += 1
    return text[start:i].strip(), i


def infer_arxiv_venue(note: str, url: str) -> str:
    text = f"{note} {url}".lower()
    if "arxiv" in text:
        return "arXiv"
    return ""


def keyword_list(fields: dict[str, str]) -> list[str]:
    raw = fields.get("keywords", "")
    tags = []
    for item in re.split(r"[,;]", raw):
        item = clean_tex(item).strip()
        if not item or item == "/unread":
            continue
        tags.append(item)
    return sorted(dict.fromkeys(tags))


def collection_list(fields: dict[str, str]) -> list[str]:
    values = []
    for name in ("groups", "collection", "collections"):
        raw = fields.get(name, "")
        if not raw:
            continue
        for item in re.split(r"[,;|]", raw):
            item = clean_tex(item).strip()
            if item:
                values.append(item)
    return sorted(dict.fromkeys(values))


def collection_lookup_title(value: str) -> str:
    value = clean_tex(value).lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def collection_lookup_doi(value: str) -> str:
    value = clean_value(value).lower()
    value = value.replace("https://doi.org/", "")
    value = value.replace("http://dx.doi.org/", "")
    return value.strip()


def iter_collection_nodes(nodes: list[dict[str, object]], parents: list[str] | None = None):
    parents = parents or []
    for node in nodes:
        name = clean_tex(str(node.get("name") or "")).strip()
        if not name:
            continue
        path = parents + [name]
        yield node, path
        children = node.get("children")
        if isinstance(children, list):
            child_nodes = [child for child in children if isinstance(child, dict)]
            yield from iter_collection_nodes(child_nodes, path)


def load_collection_assignments(path: Path) -> tuple[dict[str, list[str]], dict[str, int]]:
    assignments: dict[str, set[str]] = defaultdict(set)
    stats = {
        "collection_count": 0,
        "item_memberships": 0,
        "unique_items": 0,
    }
    if not path.exists():
        return {}, stats
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Collection JSON must be a list of Zotero collections: {path}")
    seen_items: set[str] = set()
    for node, path_parts in iter_collection_nodes(data):
        stats["collection_count"] += 1
        collection_path = " / ".join(path_parts)
        items = node.get("items")
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            stats["item_memberships"] += 1
            item_identity = str(item.get("zotero_key") or item.get("citation_key") or item.get("title") or "")
            if item_identity:
                seen_items.add(item_identity)
            citation_key = clean_value(str(item.get("citation_key") or ""))
            if citation_key:
                assignments[f"citation:{citation_key}"].add(collection_path)
            doi = collection_lookup_doi(str(item.get("doi") or ""))
            if doi:
                assignments[f"doi:{doi}"].add(collection_path)
            title = collection_lookup_title(str(item.get("title") or ""))
            if title:
                assignments[f"title:{title}"].add(collection_path)
    stats["unique_items"] = len(seen_items)
    return {key: sorted(values) for key, values in assignments.items()}, stats


def apply_collection_assignments(
    papers: list[Paper],
    assignments: dict[str, list[str]],
    source_label: str,
) -> int:
    matched = 0
    for paper in papers:
        collections: set[str] = set(paper.collections)
        for lookup_key in (
            f"citation:{paper.key}",
            f"doi:{collection_lookup_doi(paper.doi)}",
            f"title:{collection_lookup_title(paper.title)}",
        ):
            collections.update(assignments.get(lookup_key, []))
        if collections:
            if not paper.collections:
                matched += 1
            paper.collections = sorted(collections)
            paper.fields["_collection_source"] = source_label
    return matched


def infer_list(text: str, patterns: list[tuple[str, list[str]]]) -> list[str]:
    found = []
    haystack = text.lower()
    for label, keys in patterns:
        if any(re.search(key, haystack) for key in keys):
            found.append(label)
    return found or [UNVERIFIED]


def has_brain_signal_evidence(text: str) -> bool:
    haystack = text.lower()
    patterns = [
        r"\bbrain\b",
        r"\beeg\b",
        r"\bfmri\b",
        r"\bmeg\b",
        r"\bieeg\b",
        r"\becog\b",
        r"\bbci\b",
        r"\bvoxel",
        r"\bcortex\b",
        r"\bcortical\b",
        r"\bneuroimaging\b",
        r"\bneural (signal|signals|recording|recordings|activity|response|responses|data|decoding|encoding)\b",
        r"\bintracranial\b",
        r"\belectroencephal",
        r"\bmagnetoencephal",
    ]
    return any(re.search(pattern, haystack) for pattern in patterns)


NEURAL_ONLY_TASKS = {
    "Neural decoding",
    "Encoding model",
    "Visual reconstruction",
    "Speech/language decoding",
    "Closed-loop BCI",
    "Emotion/cognitive state recognition",
}


def filter_tasks_for_source_evidence(tasks: list[str], text: str) -> list[str]:
    if has_brain_signal_evidence(text):
        return tasks
    filtered = [task for task in tasks if task not in NEURAL_ONLY_TASKS]
    return filtered or [UNVERIFIED]


MODALITY_PATTERNS = [
    ("EEG", [r"\beeg\b", r"electroencephal"]),
    ("fMRI", [r"\bfmri\b", r"functional magnetic resonance", r"\bvoxel"]),
    ("MEG", [r"\bmeg\b", r"magneto"]),
    ("iEEG/ECoG", [r"\bieeg\b", r"\becog\b", r"electrocortic"]),
    ("LFP", [r"\blfp\b", r"local field potential"]),
    ("Spike", [r"\bspike", r"spiking", r"single[- ]unit"]),
    ("Multimodal neural data", [r"multimodal", r"multi-modal", r"cross-modal"]),
    ("Non-neural AI baseline", [r"imagenet", r"vision transformer", r"\bbert\b", r"language model"]),
]

TASK_PATTERNS = [
    ("Neural decoding", [r"decod", r"brain-to", r"brain reading"]),
    ("Encoding model", [r"encod", r"voxelwise", r"brain mapping"]),
    ("Visual reconstruction", [r"reconstruct", r"image generation", r"brain-to-image", r"visual"]),
    ("Speech/language decoding", [r"speech", r"language", r"semantic", r"listening"]),
    ("Representation alignment", [r"align", r"latent space", r"representation"]),
    ("Closed-loop BCI", [r"closed[- ]loop", r"stimulation", r"feedback"]),
    ("Emotion/cognitive state recognition", [r"emotion", r"affective", r"workload", r"cognitive"]),
    ("Foundation model/pretraining", [r"foundation model", r"pretrain", r"self-supervised", r"masked"]),
    ("Dataset/benchmark", [r"dataset", r"benchmark", r"bids", r"large-scale"]),
    ("Continual/adaptive learning", [r"continual", r"incremental", r"domain adaptation", r"cross-subject"]),
]

METHOD_PATTERNS = [
    ("Transformer", [r"transformer", r"\bvit\b", r"attention"]),
    ("Large language model", [r"\bllm\b", r"large language", r"\bbert\b", r"language model"]),
    ("Diffusion/generative model", [r"diffusion", r"score-based", r"generative"]),
    ("Contrastive learning", [r"contrastive", r"\bclip\b", r"clap"]),
    ("Masked autoencoder/pretraining", [r"masked", r"autoencoder", r"pretrain", r"self-supervised"]),
    ("Variational autoencoder", [r"\bvae\b", r"variational"]),
    ("Graph neural network", [r"\bgnn\b", r"graph neural"]),
    ("CNN/RNN deep model", [r"\bcnn\b", r"convolution", r"\brnn\b", r"\blstm\b"]),
    ("Linear/encoding baseline", [r"linear", r"ridge", r"regression"]),
    ("Reinforcement learning/bandit", [r"reinforcement", r"bandit", r"\brl\b"]),
]

DATASET_PATTERNS = [
    ("Natural Scenes Dataset (NSD)", [r"natural scenes dataset", r"\bnsd\b"]),
    ("THINGS", [r"things-eeg", r"things-data", r"things eeg", r"things stimulus", r"1,854 object", r"human eeg recordings for 1,854"]),
    ("DEAP", [r"\bdeap\b"]),
    ("SEED/SEED-IV", [r"\bseed\b", r"seed-iv"]),
    ("DREAMER", [r"\bdreamer\b"]),
    ("BCI Competition", [r"bci competition"]),
    ("MEG-MASC", [r"meg-masc"]),
    ("MOUS", [r"\bmous\b", r"mother of unification studies"]),
    ("ZuCo", [r"\bzuco\b"]),
    ("HBN-EEG", [r"\bhbn-eeg\b", r"healthy brain network"]),
    ("CineBrain", [r"\bcinebrain\b"]),
    ("Brennan/Hale naturalistic language data", [r"naturalistic stories", r"story listening"]),
    ("Narratives/fMRI language datasets", [r"short stories", r"listening to stories", r"natural language fmri"]),
    ("Allen Brain Observatory / mouse V1", [r"allen brain observatory", r"mouse v1"]),
]

DOMAIN_RULES = [
    ("BCI-EEG decoding", ["EEG", "Neural decoding"]),
    ("Brain image reconstruction", ["Visual reconstruction"]),
    ("Neural language and speech", ["Speech/language decoding"]),
    ("Neural foundation models", ["Foundation model/pretraining"]),
    ("Brain-model alignment", ["Representation alignment"]),
    ("Closed-loop BCI", ["Closed-loop BCI"]),
    ("fMRI visual/language modeling", ["fMRI"]),
    ("MEG/iEEG/spike decoding", ["MEG", "iEEG/ECoG", "Spike", "LFP"]),
    ("Emotion and cognitive state BCI", ["Emotion/cognitive state recognition"]),
    ("Datasets and benchmarks", ["Dataset/benchmark"]),
    ("General ML/AI methods", ["Non-neural AI baseline"]),
]


def enrich(papers: list[Paper]) -> None:
    for paper in papers:
        paper.tags = keyword_list(paper.fields)
        paper.collections = collection_list(paper.fields)
        text = " ".join(
            [
                paper.title,
                paper.fields.get("abstract", ""),
                paper.fields.get("keywords", ""),
                paper.fields.get("journal", ""),
                paper.fields.get("booktitle", ""),
                paper.fields.get("note", ""),
            ]
        )
        paper.modalities = infer_list(text, MODALITY_PATTERNS)
        paper.tasks = filter_tasks_for_source_evidence(infer_list(text, TASK_PATTERNS), text)
        paper.methods = infer_list(text, METHOD_PATTERNS)
        paper.datasets = infer_list(text, DATASET_PATTERNS)
        paper.domains = infer_domains(paper)


def infer_domains(paper: Paper) -> list[str]:
    if "Non-neural AI baseline" in paper.modalities and not has_brain_signal_evidence(evidence_text(paper)):
        return ["General ML/AI methods"]
    labels = set(paper.modalities + paper.tasks)
    domains = [domain for domain, required in DOMAIN_RULES if any(item in labels for item in required)]
    return domains or ["General AI x neuroscience reference"]


def load_cache(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_cache(path: Path, cache: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def openalex_url_for(paper: Paper) -> str:
    doi = clean_value(paper.fields.get("doi", "")).replace("https://doi.org/", "")
    if doi and doi != UNVERIFIED:
        return "https://api.openalex.org/works/" + urllib.parse.quote("https://doi.org/" + doi, safe="")
    title = clean_tex(paper.fields.get("title", ""))
    if title:
        query = urllib.parse.urlencode({"search": title, "per-page": "1"})
        return "https://api.openalex.org/works?" + query
    return ""


def fetch_openalex(paper: Paper, cache: dict[str, object], delay: float, timeout: float) -> dict[str, object]:
    cache_key = clean_value(paper.fields.get("doi", "")) or clean_tex(paper.fields.get("title", "")) or paper.key
    if cache_key in cache:
        cached = cache[cache_key]
        if isinstance(cached, dict) and openalex_match_is_safe(paper, cached):
            return cached
        return {}
    url = openalex_url_for(paper)
    if not url:
        cache[cache_key] = {}
        return {}
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "NeuroFlow-Agent Zotero importer; public metadata enrichment",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        cache[cache_key] = {}
        return {}
    if "results" in data and isinstance(data.get("results"), list):
        data = data["results"][0] if data["results"] else {}
    if not openalex_match_is_safe(paper, data):
        cache[cache_key] = {}
        return {}
    keep = {
        "id": data.get("id"),
        "doi": data.get("doi"),
        "title": data.get("title"),
        "publication_year": data.get("publication_year"),
        "type": data.get("type"),
        "primary_location": data.get("primary_location"),
        "authorships": data.get("authorships"),
        "concepts": data.get("concepts"),
        "open_access": data.get("open_access"),
        "cited_by_count": data.get("cited_by_count"),
    }
    cache[cache_key] = keep
    if delay:
        time.sleep(delay)
    return keep


def normalize_title_for_match(title: str) -> set[str]:
    title = clean_tex(title).lower()
    words = re.findall(r"[a-z0-9]+", title)
    return {word for word in words if len(word) > 2}


def openalex_match_is_safe(paper: Paper, data: dict[str, object]) -> bool:
    doi = clean_value(paper.fields.get("doi", "")).lower().replace("https://doi.org/", "")
    returned_doi = clean_value(str(data.get("doi", ""))).lower().replace("https://doi.org/", "")
    if doi:
        return bool(returned_doi and returned_doi == doi)
    source_title = normalize_title_for_match(paper.fields.get("title", ""))
    returned_title = normalize_title_for_match(str(data.get("title", "")))
    if not source_title or not returned_title:
        return False
    overlap = len(source_title & returned_title) / max(len(source_title), len(returned_title))
    return overlap >= 0.75


def enrich_web_metadata(papers: list[Paper], cache_path: Path, delay: float, timeout: float, limit: int | None) -> None:
    cache = load_cache(cache_path)
    count = 0
    for paper in papers:
        if limit is not None and count >= limit:
            break
        paper.web = fetch_openalex(paper, cache, delay, timeout)
        count += 1
        if count % 25 == 0:
            save_cache(cache_path, cache)
            print(f"OpenAlex enriched {count} papers...")
    save_cache(cache_path, cache)


def web_concepts(paper: Paper) -> list[str]:
    concepts = paper.web.get("concepts")
    if not isinstance(concepts, list):
        return []
    names = []
    for concept in concepts[:8]:
        if isinstance(concept, dict) and concept.get("display_name"):
            names.append(str(concept["display_name"]))
    return names


def contribution_statement(paper: Paper) -> str:
    parts = []
    if paper.methods != [UNVERIFIED]:
        parts.append("methods: " + ", ".join(paper.methods[:3]))
    if paper.tasks != [UNVERIFIED]:
        parts.append("tasks: " + ", ".join(paper.tasks[:3]))
    if paper.modalities != [UNVERIFIED]:
        parts.append("modalities: " + ", ".join(paper.modalities[:3]))
    concepts = web_concepts(paper)
    if concepts:
        parts.append("OpenAlex concepts: " + ", ".join(concepts[:4]))
    if not parts:
        return NOT_IDENTIFIED
    return "Auto-inferred area: " + "; ".join(parts) + "."


def evidence_statement(paper: Paper) -> str:
    sources = ["Zotero BIB"]
    if paper.web:
        sources.append("OpenAlex")
    return "Sources: " + ", ".join(sources) + "; verify paper before citation-critical use."


def citation_guardrail(paper: Paper) -> str:
    guards = ["claims beyond verified metadata"]
    if paper.modalities == [UNVERIFIED]:
        guards.append("modality-specific claims")
    if paper.datasets == [UNVERIFIED]:
        guards.append("dataset-specific claims")
    if paper.methods == [UNVERIFIED]:
        guards.append("method-specific novelty claims")
    return "; ".join(guards) + "."


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def paper_ref(paper: Paper) -> str:
    year = paper.year if paper.year != UNVERIFIED else "n.d."
    return f"{paper.title} ({year})"


def compact_values(values: list[str], fallback: str) -> str:
    clean = [value for value in values if value and value != UNVERIFIED]
    return ", ".join(clean) if clean else fallback


def metadata_values(values: list[str]) -> str:
    return compact_values(values, NOT_IDENTIFIED)


def evidence_text(paper: Paper) -> str:
    return ". ".join(
        [
            paper.title,
            clean_tex(paper.fields.get("abstract", "")),
            clean_tex(paper.fields.get("keywords", "")),
        ]
    )


def sentence_split(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def find_evidence_sentence(paper: Paper, patterns: list[str]) -> str:
    sentences = sentence_split(evidence_text(paper))
    for sentence in sentences:
        haystack = sentence.lower()
        if any(re.search(pattern, haystack) for pattern in patterns):
            return sentence[:420]
    return MANUAL_CHECK


def exact_or_review(sentence: str) -> str:
    if sentence == MANUAL_CHECK:
        return MANUAL_CHECK
    return sentence


def evidence_class(sentence: str) -> str:
    if sentence == MANUAL_CHECK:
        return "unsupported by imported metadata; manual paper inspection required"
    return "direct sentence from BIB title/abstract/keywords"


def sentence_contains_any(sentence: str, patterns: list[str]) -> bool:
    haystack = sentence.lower()
    return any(re.search(pattern, haystack) for pattern in patterns)


def result_sentence(paper: Paper) -> str:
    patterns = [
        r"\bwe (show|demonstrate|find|report|reveal|achieve|outperform|improve)",
        r"\bour (results|experiments|evaluation|method|model|approach) (show|demonstrate|indicate|achieve|outperform|improve)",
        r"\bresults (show|demonstrate|indicate)",
        r"\bexperiments (show|demonstrate|indicate)",
        r"\boutperform",
        r"\bstate-of-the-art",
        r"\bachiev(e|es|ed|ing)\b",
        r"\bimprov(e|es|ed|ing)\b",
        r"\btop-1\b",
        r"\baccuracy\b",
    ]
    return find_evidence_sentence(paper, patterns)


def limitation_sentence(paper: Paper) -> str:
    patterns = [
        r"\bhowever\b",
        r"\blimitation",
        r"\bfail(s|ed|ing)?\b",
        r"\bcannot\b",
        r"\bconstrain(ed|t)?\b",
        r"\blow signal\b",
        r"\bsmall (sample|dataset|number|cohort)",
        r"\black(s|ed|ing)?\b",
        r"\bonly\b",
    ]
    return find_evidence_sentence(paper, patterns)


def method_detail(paper: Paper, method: str) -> str:
    patterns = METHOD_PATTERN_LOOKUP.get(method, [])
    return find_evidence_sentence(paper, patterns)


def dataset_detail(paper: Paper, dataset: str) -> str:
    patterns = DATASET_PATTERN_LOOKUP.get(dataset, [])
    dataset_sentence = find_evidence_sentence(paper, patterns)
    if dataset_sentence == MANUAL_CHECK:
        return MANUAL_CHECK
    use_patterns = [
        r"\b(using|used|uses|evaluate|evaluated|benchmark|trained|tested|collected|recorded|presented|contains|comprises)\b",
        r"\bdataset\b",
        r"\bdatabase\b",
        r"\brecordings?\b",
    ]
    if sentence_contains_any(dataset_sentence, use_patterns):
        return dataset_sentence
    return MANUAL_CHECK


def task_detail(paper: Paper) -> str:
    if paper.tasks == [UNVERIFIED]:
        return MANUAL_CHECK
    patterns = []
    for task in paper.tasks:
        patterns.extend(TASK_PATTERN_LOOKUP.get(task, []))
    sentence = find_evidence_sentence(paper, patterns)
    if sentence == MANUAL_CHECK:
        return MANUAL_CHECK
    labels = ", ".join(task for task in paper.tasks if task != UNVERIFIED)
    return f"{labels}; evidence: {sentence[:360]}"


METHOD_PATTERN_LOOKUP = {label: keys for label, keys in METHOD_PATTERNS}
DATASET_PATTERN_LOOKUP = {label: keys for label, keys in DATASET_PATTERNS}
TASK_PATTERN_LOOKUP = {label: keys for label, keys in TASK_PATTERNS}


def method_macro(method: str) -> str:
    mapping = {
        "Diffusion/generative model": "Generative modeling",
        "Transformer": "Sequence and attention architectures",
        "Large language model": "Language and multimodal foundation models",
        "Contrastive learning": "Cross-modal representation alignment",
        "Masked autoencoder/pretraining": "Self-supervised neural representation learning",
        "Variational autoencoder": "Latent variable modeling",
        "Graph neural network": "Graph-based neural signal modeling",
        "CNN/RNN deep model": "Deep temporal/spatial neural decoding",
        "Linear/encoding baseline": "Classical encoding and baseline models",
        "Reinforcement learning/bandit": "Closed-loop optimization and adaptive control",
    }
    return mapping.get(method, "Other evidence-linked methods")


def dataset_modality(dataset: str) -> str:
    mapping = {
        "Natural Scenes Dataset (NSD)": "fMRI",
        "THINGS": "EEG/fMRI stimulus-aligned visual cognition",
        "DEAP": "EEG and peripheral physiological signals",
        "SEED/SEED-IV": "EEG",
        "DREAMER": "EEG and ECG",
        "BCI Competition": "BCI neural signals",
        "MEG-MASC": "MEG",
        "MOUS": "MRI, fMRI, and MEG",
        "ZuCo": "EEG and eye-tracking",
        "HBN-EEG": "EEG",
        "CineBrain": "multimodal brain data",
        "Brennan/Hale naturalistic language data": "fMRI/MEG language processing",
        "Narratives/fMRI language datasets": "fMRI",
        "Allen Brain Observatory / mouse V1": "mouse visual cortex neural activity",
    }
    return mapping.get(dataset, MANUAL_CHECK)


def build_index(papers: list[Paper]) -> str:
    lines = [
        "# Zotero Library Index",
        "",
        "Generated from private Zotero BIB metadata. Raw BIB entries, attachment paths, notes, and full abstracts are not copied into this public file.",
        "",
        f"Total parsed papers: {len(papers)}",
        "",
    ]
    for paper in papers:
        lines.extend(
            [
                f"## {paper.title}",
                "",
                f"Venue/year: {paper.venue} / {paper.year}",
                f"Authors: {paper.authors}",
                f"DOI: {paper.doi}",
                f"Signal modality: {metadata_values(paper.modalities)}",
                f"Task: {metadata_values(paper.tasks)}",
                f"Method: {metadata_values(paper.methods)}",
                f"Dataset: {metadata_values(paper.datasets)}",
                f"Zotero Collection: {metadata_values(paper.collections)}",
                f"Metric: {NOT_IDENTIFIED}",
                f"Code/data: {public_code_data(paper)}",
                f"Main claim: {contribution_statement(paper)}",
                f"Evidence: {evidence_statement(paper)}",
                f"Limitations: {NOT_IDENTIFIED}; inspect paper.",
                f"Relation to AI x neuroscience workflow: {', '.join(paper.domains)}",
                f"Use when: {use_when(paper)}",
                f"Do not cite for: {citation_guardrail(paper)}",
                f"Verification status: auto-imported; verify before citation-critical use.",
                "",
            ]
        )
    return "\n".join(lines)


def public_code_data(paper: Paper) -> str:
    url = clean_value(paper.fields.get("url", ""))
    if url.startswith("http"):
        return url
    return NOT_IDENTIFIED


def use_when(paper: Paper) -> str:
    bits = []
    if paper.domains:
        bits.append("; ".join(paper.domains[:3]))
    if paper.methods and paper.methods != [UNVERIFIED]:
        bits.append("method: " + ", ".join(paper.methods[:3]))
    if paper.datasets and paper.datasets != [UNVERIFIED]:
        bits.append("dataset: " + ", ".join(paper.datasets[:3]))
    return " | ".join(bits) if bits else NOT_IDENTIFIED


def build_taxonomy(papers: list[Paper]) -> str:
    by_domain: dict[str, dict[str, dict[str, list[Paper]]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    tag_counter: Counter[str] = Counter()
    collection_fields = sum(1 for paper in papers if paper.collections)
    use_collections = collection_fields > 0
    collection_sources = sorted(
        {
            clean_value(str(paper.fields.get("_collection_source", "BIB collection/group fields")))
            for paper in papers
            if paper.collections
        }
    )
    for paper in papers:
        primary_domains = (
            paper.collections
            if use_collections and paper.collections
            else [domain for domain in paper.domains if domain != "General AI x neuroscience reference"] or ["Unassigned / requires collection recovery"]
        )
        tasks = [task for task in paper.tasks if task != UNVERIFIED] or ["Task requires manual verification"]
        methods = [method for method in paper.methods if method != UNVERIFIED] or ["Method requires manual verification"]
        for domain in primary_domains:
            for task in tasks:
                for method in methods:
                    by_domain[domain][task][method].append(paper)
        tag_counter.update(paper.tags)

    lines = [
        "# Paper Taxonomy",
        "",
        "High-precision taxonomy policy: authoritative collection alignment requires Zotero-native Collection membership from BIB collection/group fields or the private Zotero collection export JSON. When Collection evidence is present, Collection paths are preserved and not merged or renamed by AI inference.",
        "",
        "## Collection Provenance Audit",
        "",
        f"- Parsed papers: {len(papers)}",
        f"- Papers with Zotero Collection assignments: {collection_fields}",
        f"- Collection assignment source: {', '.join(collection_sources) if collection_sources else MANUAL_CHECK}",
        "- Collection-aligned taxonomy status: authoritative Zotero Collection tree generated." if use_collections else "- Collection-aligned taxonomy status: 待人工核验补充; re-export from Zotero/Better BibTeX with collection/group metadata to make this authoritative.",
        "",
        "## Zotero Collection Taxonomy" if use_collections else "## Provisional Content-Derived Taxonomy",
        "",
    ]
    for domain, task_map in sorted(by_domain.items(), key=lambda kv: (-sum(len(papers) for method_map in kv[1].values() for papers in method_map.values()), kv[0])):
        lines.extend([f"### {domain}", ""])
        for task, method_map in sorted(task_map.items(), key=lambda kv: (-sum(len(papers) for papers in kv[1].values()), kv[0])):
            lines.extend([f"#### {task}", ""])
            for method, items in sorted(method_map.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:8]:
                lines.extend([f"##### {method}", "", f"Count: {len(items)}", ""])
                for paper in sorted(items, key=lambda p: (p.year == UNVERIFIED, p.year, p.title), reverse=True)[:5]:
                    lines.append(
                        f"- {paper_ref(paper)} | collection source: {paper.fields.get('_collection_source', MANUAL_CHECK)} | content evidence: {task_detail(paper)}"
                    )
                if len(items) > 5:
                    lines.append(f"- ... {len(items) - 5} more in `zotero-library-index.md`")
                lines.append("")
    lines.extend(["## Frequent Zotero Tags", ""])
    for tag, count in tag_counter.most_common(50):
        lines.append(f"- {tag}: {count}")
    return "\n".join(lines)


def build_method_map(papers: list[Paper]) -> str:
    grouped: dict[str, dict[str, list[tuple[Paper, str]]]] = defaultdict(lambda: defaultdict(list))
    unresolved = 0
    for paper in papers:
        for method in paper.methods:
            if method == UNVERIFIED:
                unresolved += 1
                continue
            detail = method_detail(paper, method)
            grouped[method_macro(method)][method].append((paper, detail))
    lines = [
        "# Method Map",
        "",
        "High-precision policy: entries are attached only when the paper title, abstract, or keywords contain method evidence. Generic strengths, weaknesses, and comparisons are not invented; unsupported cells are marked `待人工核验补充`.",
        "",
        f"Unresolved method assignments: {unresolved}",
        "",
    ]
    for macro, method_map in sorted(grouped.items(), key=lambda kv: kv[0]):
        lines.extend([f"## {macro}", ""])
        for method, items in sorted(method_map.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            lines.extend([f"### {method}", "", f"Linked papers: {len(items)}", ""])
            for paper, detail in items[:35]:
                lines.extend(
                    [
                        f"#### {paper_ref(paper)}",
                        f"- Core algorithm / architecture / technical point: {detail}",
                        f"- Core-method evidence class: {evidence_class(detail)}",
                        f"- Applicable task scenario: {task_detail(paper)}",
                        f"- Paper-specific reported advantage: {result_sentence(paper)}",
                        f"- Paper-specific limitation / caveat: {limitation_sentence(paper)}",
                        f"- Difference from contemporary related methods: {MANUAL_CHECK}",
                        f"- Evidence source: BIB title/abstract/keywords; citation-critical use requires paper inspection.",
                        "",
                    ]
                )
            if len(items) > 35:
                lines.append(f"Additional linked papers requiring expansion: {len(items) - 35}. See `zotero-library-index.md`.\n")
    return "\n".join(lines)


def build_dataset_map(papers: list[Paper]) -> str:
    by_dataset: dict[str, list[Paper]] = defaultdict(list)
    unresolved = 0
    for paper in papers:
        for dataset in paper.datasets:
            if dataset == UNVERIFIED:
                unresolved += 1
                continue
            by_dataset[dataset].append(paper)
    lines = [
        "# Dataset Map",
        "",
        "High-precision policy: this file only includes neural, BCI, EEG, fMRI, MEG, iEEG/ECoG, spike, or closely related neuroimaging datasets explicitly detected in the paper title/abstract/keywords. Non-neural generic ML datasets are excluded.",
        "",
        f"Unresolved dataset assignments: {unresolved}",
        "",
    ]
    for dataset, items in sorted(by_dataset.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lines.extend(
            [
                f"## {dataset}",
                "",
                f"- Full name: {dataset}",
                f"- Official data specification: {dataset_spec(dataset, items)}",
                f"- Modality: {dataset_modality(dataset)}",
                f"- Suitable tasks: {summarize_values(items, 'tasks')}",
                f"- Open status and access route: {dataset_access(dataset, items)}",
                f"- Appropriate use: {dataset_use(dataset, items)}",
                f"- Inappropriate use: {MANUAL_CHECK}",
                "",
                "### Citation Sources",
                "",
            ]
        )
        for paper in items[:40]:
            lines.extend(
                [
                    f"#### {paper_ref(paper)}",
                    f"- Evidence that the dataset is used or introduced: {dataset_detail(paper, dataset)}",
                    f"- Dataset evidence class: {evidence_class(dataset_detail(paper, dataset))}",
                    f"- Task context: {task_detail(paper)}",
                    "",
                ]
            )
        if len(items) > 40:
            lines.append(f"Additional citing papers requiring expansion: {len(items) - 40}. See `zotero-library-index.md`.\n")
    return "\n".join(lines)


def summarize_values(papers: list[Paper], attr: str) -> str:
    counter: Counter[str] = Counter()
    for paper in papers:
        counter.update(value for value in getattr(paper, attr) if value != UNVERIFIED)
    values = [name for name, _ in counter.most_common(5)]
    return ", ".join(values) if values else NOT_IDENTIFIED


def dataset_spec(dataset: str, items: list[Paper]) -> str:
    for paper in items:
        sentence = dataset_detail(paper, dataset)
        if sentence != MANUAL_CHECK and re.search(r"\b(\d+|subjects?|participants?|hours?|sessions?|recordings?|trials?)\b", sentence, re.I):
            return sentence[:420]
    return MANUAL_CHECK


def dataset_access(dataset: str, items: list[Paper]) -> str:
    for paper in items:
        sentence = find_evidence_sentence(
            paper,
            [
                r"publicly available",
                r"openly available",
                r"available at",
                r"\bdata are available\b",
                r"\bbids\b",
                r"\bgithub\b",
                r"\bosf\b",
                r"\bopen-access\b",
            ],
        )
        if sentence != MANUAL_CHECK:
            return sentence[:420]
    return MANUAL_CHECK


def dataset_use(dataset: str, items: list[Paper]) -> str:
    tasks = summarize_values(items, "tasks")
    if tasks == NOT_IDENTIFIED:
        return MANUAL_CHECK
    return tasks


def build_claim_map(papers: list[Paper]) -> str:
    by_cluster: dict[str, list[Paper]] = defaultdict(list)
    for paper in papers:
        domains = [domain for domain in paper.domains if domain != "General AI x neuroscience reference"] or ["Unclustered claims requiring verification"]
        for domain in domains[:3]:
            by_cluster[domain].append(paper)
    lines = [
        "# Claim-to-Citation Map",
        "",
        "High-precision policy: each claim entry is anchored to a single paper's abstract/title metadata. Cross-paper synthesis is limited to clustering similar claim types; do not treat cluster membership as a shared conclusion.",
        "",
        "## Field Definitions",
        "",
        "- Domain consensus: repeated claim pattern across multiple papers; requires separate review before being written as consensus.",
        "- Single-paper original claim: a paper-specific conclusion extracted from its abstract/title metadata.",
        "",
    ]
    for cluster, items in sorted(by_cluster.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lines.extend([f"## Cluster: {cluster}", "", f"- Candidate papers: {len(items)}", f"- Consensus status: {MANUAL_CHECK}", ""])
        for paper in items[:45]:
            claim = result_sentence(paper)
            evidence = task_detail(paper)
            weak = limitation_sentence(paper)
            careful = (
                f"This paper reports that {claim[0].lower() + claim[1:]}"
                if claim != MANUAL_CHECK
                else MANUAL_CHECK
            )
            lines.extend(
                [
                    f"### {paper_ref(paper)}",
                    f"- Single-paper original claim: {claim}",
                    f"- Claim evidence class: {evidence_class(claim)}",
                    f"- Direct supporting experiment/data basis: {evidence}",
                    f"- Weakness in support: {weak}",
                    f"- Likely reviewer risk: {reviewer_risk(paper)}",
                    f"- Careful writing form: {careful}",
                    f"- Do not overuse for: {citation_guardrail(paper)}",
                    "",
                ]
            )
        if len(items) > 45:
            lines.append(f"Additional papers in this claim cluster requiring expansion: {len(items) - 45}. See `zotero-library-index.md`.\n")
    return "\n".join(lines)


def reviewer_risk(paper: Paper) -> str:
    risks = []
    if paper.datasets == [UNVERIFIED]:
        risks.append("dataset and split protocol not identified from metadata")
    if paper.modalities == [UNVERIFIED]:
        risks.append("neural modality not identified from metadata")
    if "Closed-loop BCI" in paper.tasks:
        risks.append("online versus offline closed-loop validity must be checked")
    if "Visual reconstruction" in paper.tasks:
        risks.append("qualitative reconstruction evidence may be insufficient")
    if "Foundation model/pretraining" in paper.tasks:
        risks.append("cross-subject/session generalization must be verified")
    return "; ".join(risks) if risks else MANUAL_CHECK


def unresolved_fields(paper: Paper) -> list[str]:
    fields = []
    if paper.title == UNVERIFIED:
        fields.append("title")
    if paper.year == UNVERIFIED:
        fields.append("year")
    if paper.venue == UNVERIFIED:
        fields.append("venue")
    if paper.doi == UNVERIFIED:
        fields.append("doi")
    if paper.authors == UNVERIFIED:
        fields.append("authors")
    if paper.modalities == [UNVERIFIED]:
        fields.append("signal modality")
    if paper.tasks == [UNVERIFIED]:
        fields.append("task")
    if paper.methods == [UNVERIFIED]:
        fields.append("method")
    if paper.datasets == [UNVERIFIED]:
        fields.append("dataset")
    fields.extend(["metric", "limitations"])
    return fields


def build_manual_review_report(papers: list[Paper]) -> str:
    unresolved_counter: Counter[str] = Counter()
    rows = []
    for paper in papers:
        missing = unresolved_fields(paper)
        unresolved_counter.update(missing)
        if missing:
            rows.append((paper, missing))
    lines = [
        "# Manual Review Needed",
        "",
        "This report lists fields that could not be verified from cleaned Zotero BIB metadata or OpenAlex public metadata. Fill these only after inspecting the paper or a trusted public source.",
        "",
        "## Summary",
        "",
    ]
    for field_name, count in unresolved_counter.most_common():
        lines.append(f"- {field_name}: {count}")
    lines.extend(["", "## Priority Entries", ""])
    priority = sorted(rows, key=lambda item: (-len(item[1]), item[0].title))[:300]
    for paper, missing in priority:
        lines.extend(
            [
                f"### {paper.title}",
                "",
                f"Year: {paper.year}",
                f"Venue: {paper.venue}",
                f"DOI: {paper.doi}",
                f"Missing or unresolved: {', '.join(missing)}",
                f"Suggested next action: search by DOI or exact title, then update the relevant index/map fields if verified.",
                "",
            ]
        )
    if len(rows) > len(priority):
        lines.append(f"Additional entries needing review: {len(rows) - len(priority)}. Use `zotero-library-index.md` for the full list.")
    return "\n".join(lines)


def build_private_readme(source: Path, papers: list[Paper], collections_source: Path | None, collection_stats: dict[str, int]) -> str:
    return "\n".join(
        [
            "# Zotero Private Import Notes",
            "",
            "This private file records local import bookkeeping only. Do not move raw BIB exports, attachment paths, personal notes, or unpublished project judgments into public skill references.",
            "",
            f"Source BIB: {source.name}",
            f"Collection export JSON: {collections_source.name if collections_source else NOT_IDENTIFIED}",
            f"Parsed entries: {len(papers)}",
            f"Collection nodes parsed: {collection_stats.get('collection_count', 0)}",
            f"Collection item memberships parsed: {collection_stats.get('item_memberships', 0)}",
            f"Unique collection items parsed: {collection_stats.get('unique_items', 0)}",
            "",
            "Public outputs are generated under `skills/paper-rag-plus/references/` after private fields are stripped.",
        ]
    )


def run(
    source: Path,
    collections_json: Path | None,
    enrich_web: bool,
    cache_path: Path,
    delay: float,
    timeout: float,
    limit: int | None,
) -> None:
    text = source.read_text(encoding="utf-8", errors="replace")
    parsed_papers = parse_bib(text)
    skipped = [paper for paper in parsed_papers if not is_importable_reference(paper)]
    papers = [paper for paper in parsed_papers if is_importable_reference(paper)]
    if enrich_web:
        enrich_web_metadata(papers, cache_path, delay, timeout, limit)
    enrich(papers)
    collection_stats = {"collection_count": 0, "item_memberships": 0, "unique_items": 0}
    if collections_json and collections_json.exists():
        assignments, collection_stats = load_collection_assignments(collections_json)
        matched = apply_collection_assignments(
            papers,
            assignments,
            source_label=f"private Zotero collection export JSON: {collections_json.name}",
        )
        print(f"Matched Zotero Collection assignments for {matched} papers from {collections_json}")
    write(REFERENCES / "zotero-library-index.md", build_index(papers))
    write(REFERENCES / "paper-taxonomy.md", build_taxonomy(papers))
    write(REFERENCES / "method-map.md", build_method_map(papers))
    write(REFERENCES / "dataset-map.md", build_dataset_map(papers))
    write(REFERENCES / "claim-to-citation.md", build_claim_map(papers))
    write(REFERENCES / "manual-review-needed.md", build_manual_review_report(papers))
    write(PRIVATE_REFERENCES / "zotero-import.private.md", build_private_readme(source, papers, collections_json, collection_stats))
    (PRIVATE_ZOTERO / ".gitkeep").touch(exist_ok=True)
    print(f"Parsed {len(parsed_papers)} BIB entries from {source}")
    print(f"Imported {len(papers)} identifiable references; skipped {len(skipped)} non-reference placeholders")
    print(f"Wrote public Paper-RAG++ references to {REFERENCES}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default=str(PRIVATE_ZOTERO / "My Library.bib"),
        help="Private Zotero BIB export path.",
    )
    parser.add_argument(
        "--collections-json",
        default=str(PRIVATE_ZOTERO / "zotero_exports" / "my_library_collections.json"),
        help="Private Zotero collection export JSON path. Used to recover authoritative Collection membership.",
    )
    parser.add_argument(
        "--enrich-web",
        action="store_true",
        help="Fetch public OpenAlex metadata by DOI or title and cache results under .private/zotero/.",
    )
    parser.add_argument(
        "--openalex-cache",
        default=str(PRIVATE_ZOTERO / "openalex-cache.json"),
        help="Private OpenAlex metadata cache path.",
    )
    parser.add_argument(
        "--request-delay",
        type=float,
        default=0.0,
        help="Delay between OpenAlex requests in seconds.",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=6.0,
        help="OpenAlex request timeout in seconds.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional maximum number of entries to enrich; useful for testing.",
    )
    args = parser.parse_args()
    source = Path(args.input)
    if not source.exists():
        raise SystemExit(f"Input BIB not found: {source}")
    if ".private" not in source.parts:
        raise SystemExit("Refusing to import from a non-private path. Put raw Zotero exports under .private/.")
    collections_json = Path(args.collections_json) if args.collections_json else None
    if collections_json and collections_json.exists() and ".private" not in collections_json.parts:
        raise SystemExit("Refusing to import Collection JSON from a non-private path. Put raw Zotero exports under .private/.")
    run(source, collections_json, args.enrich_web, Path(args.openalex_cache), args.request_delay, args.request_timeout, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
