.DEFAULT_GOAL := help

RUN := uv run
APP_NAME := app_name
SRC_DIR := src
TEST_DIR := tests

.PHONY: help install dev-install setup update run shell test lint format check build clean

# -------------------------
# HELP
# -------------------------

help:
	@echo "📖 Usage: make [command]"
	@echo ""
	@echo "Core:"
	@echo "  install        Install runtime dependencies"
	@echo "  dev-install    Install dev dependencies (tools, tests, lint)"
	@echo "  setup          Setup git hooks (pre-commit)"
	@echo ""
	@echo "Dev:"
	@echo "  run            Run application (module mode)"
	@echo "  shell          Open Python shell"
	@echo "  test           Run tests"
	@echo "  lint           Run linter (ruff)"
	@echo "  format         Format code (ruff)"
	@echo "  typecheck      Run MyPy"
	@echo "  check          Run lint + test"
	@echo ""
	@echo "Other:"
	@echo "  update         Update dependencies"
	@echo "  build          Build package"
	@echo "  clean          Clean cache files"

# -------------------------
# INSTALLATION
# -------------------------

install:
	@echo "📦 Installing runtime dependencies..."
	uv sync

dev-install: install
	@echo "🧪 Installing development dependencies..."
	uv sync --dev

setup: dev-install
	@echo "🧩 Setup for development environment..."
	pre-commit install || true
	pre-commit install --hook-type commit-msg || true
	cp .env.example .env

update:
	@echo "🔄 Updating dependencies..."
	uv lock --upgrade
	uv sync --dev

# -------------------------
# RUNTIME
# -------------------------

run:
	@echo "🚀 Running application (module mode)..."
	$(RUN) python -m $(APP_NAME).main

shell:
	@echo "🐍 Opening Python shell..."
	$(RUN) python

# -------------------------
# QUALITY
# -------------------------

test:
	@echo "🧪 Running tests..."
	$(RUN) pytest $(TEST_DIR)

lint:
	@echo "🔍 Running Ruff..."
	$(RUN) ruff check $(SRC_DIR) $(TEST_DIR)

format:
	@echo "🎨 Formatting code..."
	$(RUN) ruff format $(SRC_DIR) $(TEST_DIR)

typecheck:
	@echo "Running MyPy..."
	$(RUN) mypy $(SRC_DIR)

check: lint test typecheck
	@echo "✅ All checks passed!"

# -------------------------
# BUILD
# -------------------------

build:
	@echo "📦 Building package..."
	uv build

# -------------------------
# CLEAN
# -------------------------

clean:
	@echo "🧹 Cleaning cache files..."
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name ".ruff_cache" -delete
	find . -type d -name "*.egg-info" -delete
	rm -rf dist/
	rm -rf build/
	@echo "✨ Clean complete"