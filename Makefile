PYTHON ?= python3

.PHONY: validate index runtime-list runtime-smoke hook-smoke kb-search install-check

validate:
	$(PYTHON) scripts/validate_skill.py

index:
	cd skills/ai-bci-research && $(PYTHON) scripts/update_knowledge_index.py --root .

runtime-list:
	$(PYTHON) scripts/neuroflow_runtime/cli.py list --kind all

runtime-smoke:
	$(PYTHON) scripts/neuroflow_runtime/cli.py run --chain paper-to-repro --task "runtime smoke test" --dry-run

hook-smoke:
	$(PYTHON) scripts/neuroflow_runtime/cli.py hook --event session_start --task "My EEG reconstruction result is worse than the baseline. What should I check next?"

kb-search:
	$(PYTHON) scripts/neuroflow_runtime/cli.py kb search "cross-subject EEG" --limit 3

install-check:
	$(PYTHON) scripts/install --target all --check
