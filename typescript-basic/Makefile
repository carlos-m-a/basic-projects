# =========================================================
# Universal Makefile Template
# =========================================================

.DEFAULT_GOAL := help

# ---------------------------------------------------------
# Setup variables
# ---------------------------------------------------------

RUN := npm # Change with bun, deno, other
APP_NAME := app_name
SRC_DIR := src
TEST_DIR := tests

.PHONY: install setup dev build run test lint format check clean ci

# Detection additional tools
DOCKER   := $(shell command -v docker)
COMPOSE  := $(shell command -v docker-compose)

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
	$(RUN) install

setup: install
	@echo "Project setup..."
	# Example:
	cp -n .env.example .env || true
	pre-commit install || true
	pre-commit install --hook-type commit-msg || true

dev:
	@echo "Starting development environment..."
	$(RUN) run dev

build:
	@echo "Building project..."
	$(RUN) run build

run:
	@echo "Running application..."
	$(RUN) start

test:
	@echo "Running tests..."
	$(RUN) run test

lint:
	@echo "Running linters..."
	$(RUN) run lint

format:
	@echo "Formatting code..."
	$(RUN) run format

check: lint test
	@echo "All checks completed."

# ---------------------------------------------------------
# Docker
# ---------------------------------------------------------

docker-build:
ifneq ($(DOCKER),)
	@echo "Building Docker image..."
	docker build -t $(APP_NAME) deploy/docker/Dockerfile .
else
	@echo "Docker not installed."
endif

docker-run:
ifneq ($(DOCKER),)
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
	rm -rf node_modules
	rm -rf coverage
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

ci: install check
	@echo "CI checks passed."
