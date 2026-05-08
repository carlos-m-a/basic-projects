# --- Configuration ---
.DEFAULT_GOAL := help
PYTHON        := uv run
APP_NAME      := python_basic # Update this to match your actual application name (the directory in src/)
SRC_DIR       := src
TEST_DIR      := tests

.PHONY: help install update run test lint format clean build shell

# --- Help System ---
help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# --- Installation ---
install: ## Install dependencies and create virtual environment
	@echo "🚀 Installing dependencies using uv..."
	uv sync

update: ## Update dependencies to their latest compatible versions
	@echo "🔄 Updating dependencies..."
	uv lock --upgrade
	uv sync

# --- Development ---
run: ## Run the application
	@echo "🏃 Starting $(APP_NAME)..."
	$(PYTHON) python $(SRC_DIR)/$(APP_NAME)/main.py

shell: ## Open a Python REPL in the current environment
	$(PYTHON) python

# --- Quality Assurance (QA) ---
test: ## Run tests using pytest
	@echo "🧪 Running tests..."
	$(PYTHON) pytest $(TEST_DIR) --cov=$(SRC_DIR) --cov-report=term-missing

lint: ## Run static analysis (Ruff)
	@echo "🔍 Linting code with Ruff..."
	$(PYTHON) ruff check $(SRC_DIR) $(TEST_DIR)

format: ## Format code (Ruff)
	@echo "🎨 Formatting code..."
	$(PYTHON) ruff format $(SRC_DIR) $(TEST_DIR)

check: lint test ## Run all checks (lint + test)

# --- Build & Distribution ---
build: ## Build the project (sdist and wheel)
	@echo "📦 Building package..."
	uv build

# --- Cleanup ---
clean: ## Remove temporary files and caches
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	rm -rf dist/ .venv/