PYTHON ?= python3

.PHONY: validate index

validate:
	$(PYTHON) scripts/validate_skill.py

index:
	cd skills/ai-bci-research && $(PYTHON) scripts/update_knowledge_index.py --root .
