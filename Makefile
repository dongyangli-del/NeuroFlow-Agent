PYTHON ?= python3

.PHONY: validate index runtime-list runtime-smoke

validate:
	$(PYTHON) scripts/validate_skill.py

index:
	cd skills/ai-bci-research && $(PYTHON) scripts/update_knowledge_index.py --root .

runtime-list:
	$(PYTHON) scripts/neuroflow_runtime/cli.py list --kind all

runtime-smoke:
	$(PYTHON) scripts/neuroflow_runtime/cli.py run --chain paper-to-repro --task "runtime smoke test" --dry-run
