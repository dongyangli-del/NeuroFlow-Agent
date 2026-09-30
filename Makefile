PYTHON ?= python3

.PHONY: validate lint test eval evolution-smoke evolution-report index runtime-list runtime-smoke hook-smoke kb-search skill-competition skill-competition-report skill-simulate install-check

validate:
	$(PYTHON) scripts/validate_skill.py

lint:
	$(PYTHON) -m ruff check scripts/neuroflow_runtime scripts/migrate_evals.py migrations tests

test:
	$(PYTHON) -m pytest --cov=neuroflow_runtime --cov-report=term --cov-fail-under=80

eval:
	$(PYTHON) scripts/neuroflow_runtime/cli.py eval run --partition protected --executor-provider mock --reviewer-provider mock

evolution-smoke:
	$(PYTHON) -m pytest tests/test_evolution.py tests/test_promotion.py

evolution-report:
	$(PYTHON) scripts/neuroflow_runtime/cli.py report evolution

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

skill-competition:
	$(PYTHON) scripts/audit_skill_competition.py

skill-competition-report:
	@$(PYTHON) scripts/audit_skill_competition.py --json

skill-simulate:
	@test -n "$(CANDIDATE)" || (echo "Usage: make skill-simulate CANDIDATE=path/to/manifest.yaml" && exit 2)
	@$(PYTHON) scripts/audit_skill_competition.py --candidate "$(CANDIDATE)"

install-check:
	$(PYTHON) scripts/install --target all --check
