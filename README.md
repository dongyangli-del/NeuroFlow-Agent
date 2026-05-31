# Codex AI x BCI Research Skill

Personal Codex skill for AI x brain-computer interface research, covering MLLMs, generative models, multimodal neural decoding, EEG visual reconstruction, brain-language alignment, closed-loop brain modulation, Physical AI, and NeuroAI.

## Install with Codex Skill Installer

On a server with Codex skills support:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo dongyangli-del/codex-ai-bci-research-skill \
  --path skills/ai-bci-research
```

Restart Codex after installation.

## Install Manually

```bash
git clone https://github.com/dongyangli-del/codex-ai-bci-research-skill.git
cd codex-ai-bci-research-skill
bash install.sh
```

For SSH:

```bash
git clone git@github.com:dongyangli-del/codex-ai-bci-research-skill.git
cd codex-ai-bci-research-skill
bash install.sh
```

## Update

```bash
cd codex-ai-bci-research-skill
git pull
bash install.sh
```

## Layout

```text
skills/ai-bci-research/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/
```

## Knowledge Update Workflow

After adding new papers, repositories, datasets, or experiment notes:

```bash
cd skills/ai-bci-research
python3 scripts/update_knowledge_index.py --root .
```

Then commit and push the changes.
