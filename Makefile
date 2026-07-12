SKILL_NAME := libllie-cli
SKILL_SOURCE := $(CURDIR)/skills/$(SKILL_NAME)
LIBLLIE_ROOT := $(CURDIR)
AGENTS_SKILL_DIR := $(HOME)/.agents/skills
AGENTS_SKILL_LINK := $(AGENTS_SKILL_DIR)/$(SKILL_NAME)
AGENTS_ENV_DIR := $(HOME)/.agents/env
AGENTS_ENV_FILE := $(AGENTS_ENV_DIR)/$(SKILL_NAME).env

ENV_ARG := $(if $(filter command line,$(origin env)),$(env),$(if $(filter command line,$(origin ENV)),$(ENV),python))
NAME_ARG := $(if $(filter command line,$(origin name)),$(name),$(if $(filter command line,$(origin NAME)),$(NAME),))

.PHONY: link-skills unlink-skills relink-skills

link-skills:
	@if [ ! -d "$(SKILL_SOURCE)" ]; then \
		echo "Missing skill source: $(SKILL_SOURCE)"; \
		exit 1; \
	fi
	@mkdir -p "$(AGENTS_SKILL_DIR)"
	@if [ -e "$(AGENTS_SKILL_LINK)" ] && [ ! -L "$(AGENTS_SKILL_LINK)" ]; then \
		echo "Refusing to replace non-symlink: $(AGENTS_SKILL_LINK)"; \
		exit 1; \
	fi
	@mkdir -p "$(AGENTS_ENV_DIR)"
	@set -e; \
	env_kind="$$(printf '%s' "$(ENV_ARG)" | tr '[:upper:]' '[:lower:]')"; \
	case "$$env_kind" in \
		uv) \
			if [ -x "$(LIBLLIE_ROOT)/.venv/bin/python" ]; then \
				python_cmd="$(LIBLLIE_ROOT)/.venv/bin/python"; \
			elif [ -x "$(LIBLLIE_ROOT)/.venv/Scripts/python.exe" ]; then \
				python_cmd="$(LIBLLIE_ROOT)/.venv/Scripts/python.exe"; \
			else \
				echo "Python environment not found for env=uv: expected $(LIBLLIE_ROOT)/.venv."; \
				exit 1; \
			fi; \
			;; \
		python) \
			command -v python >/dev/null 2>&1 || { echo "Python environment not found for env=python: python command is unavailable."; exit 1; }; \
			python_cmd="python"; \
			;; \
		conda) \
			[ -n "$(NAME_ARG)" ] || { echo "Python environment not found for env=conda: set name=<env-name>."; exit 1; }; \
			command -v conda >/dev/null 2>&1 || { echo "Python environment not found for env=conda: conda command is unavailable."; exit 1; }; \
			python_cmd="$$(conda run -n "$(NAME_ARG)" python -c 'import sys; print(sys.executable)' 2>/dev/null)" || { echo "Python environment not found for env=conda name=$(NAME_ARG)."; exit 1; }; \
			[ -x "$$python_cmd" ] || { echo "Python environment not found for env=conda name=$(NAME_ARG): $$python_cmd"; exit 1; }; \
			;; \
		*) \
			echo "Unsupported env=$(ENV_ARG). Use env=uv, env=python, or env=conda."; \
			exit 1; \
			;; \
	esac; \
	[ -n "$$python_cmd" ] || { echo "Python environment not found for env=$$env_kind."; exit 1; }; \
	tmp="$(AGENTS_ENV_FILE).tmp"; \
	if [ -f "$(AGENTS_ENV_FILE)" ]; then \
		grep -v \
			-e '^export LIBLLIE_ROOT=' \
			-e '^export LIBLLIE_PYTHON_ENV=' \
			-e '^export LIBLLIE_PYTHON=' \
			-e '^export LIBLLIE_CLI=' \
			"$(AGENTS_ENV_FILE)" > "$$tmp" || true; \
	else \
		: > "$$tmp"; \
	fi; \
	printf 'export LIBLLIE_ROOT="%s"\n' "$(LIBLLIE_ROOT)" >> "$$tmp"; \
	printf 'export LIBLLIE_PYTHON_ENV="%s"\n' "$$env_kind" >> "$$tmp"; \
	printf 'export LIBLLIE_PYTHON="%s"\n' "$$python_cmd" >> "$$tmp"; \
	printf 'export LIBLLIE_CLI="%s -m libllie.cli"\n' "$$python_cmd" >> "$$tmp"; \
	mv "$$tmp" "$(AGENTS_ENV_FILE)"
	@echo "Registered LibLLIE root and Python environment in $(AGENTS_ENV_FILE)"
	@ln -sfn "$(SKILL_SOURCE)" "$(AGENTS_SKILL_LINK)"

unlink-skills:
	@if [ -L "$(AGENTS_SKILL_LINK)" ]; then \
		rm "$(AGENTS_SKILL_LINK)"; \
	fi
	@if [ -f "$(AGENTS_ENV_FILE)" ]; then \
		rm "$(AGENTS_ENV_FILE)"; \
	fi

relink-skills:
	@$(MAKE) unlink-skills
	@$(MAKE) link-skills
