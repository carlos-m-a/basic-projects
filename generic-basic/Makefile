# =========================================================
# Universal Makefile Template
# =========================================================

.DEFAULT_GOAL := help

# ---------------------------------------------------------
# Setup variables
# ---------------------------------------------------------

RUN ?= xxx # Change
APP_NAME := app_name
SRC_DIR := src
TEST_DIR := tests

# Detection additional tools
DOCKER := $(shell command -v docker 2> /dev/null)
COMPOSE := $(shell command -v docker-compose 2> /dev/null)

# ---------------------------------------------------------
# Help
# ---------------------------------------------------------

help:
	@echo ""
	@echo "Available commands:"
	@echo ""
	@echo "  make install      Install dependencies"
	@echo "  make setup        Initial project setup"
	@echo "  make dev          Run development environment"
	@echo "  make build        Build application"
	@echo "  make run          Run application"
	@echo "  make test         Run tests"
	@echo "  make lint         Run linters"
	@echo "  make format       Format code"
	@echo "  make check        Full quality checks"
	@echo "  make clean        Clean temporary files"
	@echo "  make docker-build Build Docker image"
	@echo "  make docker-run   Run Docker container"
	@echo "  make ci           CI pipeline simulation"
	@echo ""

# ---------------------------------------------------------
# Core workflow
# ---------------------------------------------------------

install:
	@echo "Install dependencies..."
	# Language-specific:
	# npm install
	# pip install -r requirements.txt
	# cargo build

setup: install
	@echo "Project setup..."
	# Example:
	pre-commit install || true
	pre-commit install --hook-type commit-msg || true
	cp .env.example .env

dev:
	@echo "Starting development environment..."
	# npm run dev
	# python main.py

build:
	@echo "Building project..."
	# npm run build
	# cargo build --release

run:
	@echo "Running application..."
	# node src/index.js

test:
	@echo "Running tests..."
	# pytest
	# npm test

lint:
	@echo "Running linters..."
	# eslint .
	# ruff check .

format:
	@echo "Formatting code..."
	# prettier --write .
	# black .

check: lint test
	@echo "All checks completed."

# ---------------------------------------------------------
# Docker
# ---------------------------------------------------------

docker-build:
ifdef DOCKER
	@echo "Building Docker image..."
	docker build -t $(APP_NAME) .
else
	@echo "Docker not installed."
endif

docker-run:
ifdef DOCKER
	@echo "Running Docker container..."
	docker run --rm -it $(APP_NAME)
else
	@echo "Docker not installed."
endif

# ---------------------------------------------------------
# Maintenance
# ---------------------------------------------------------

clean:
	@echo "Cleaning project..."
	rm -rf .cache
	rm -rf dist
	rm -rf build
	rm -rf coverage
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

ci: install lint test
	@echo "CI checks passed."

# ---------------------------------------------------------
# Utilities
# ---------------------------------------------------------

env:
	@echo "Using env file: $(ENV_FILE)"

version:
	@echo "$(APP_NAME)"