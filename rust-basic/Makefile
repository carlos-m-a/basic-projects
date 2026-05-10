# =========================================================
# Rust Project Makefile
# =========================================================

.DEFAULT_GOAL := help

# ---------------------------------------------------------
# Setup variables
# ---------------------------------------------------------

BINARY_NAME := your_binary_name
DOCKER_FILE := deploy/docker/Dockerfile
DOCKER_IMAGE := rust-app-image

.PHONY: install setup dev build run test lint format check clean ci docker-build docker-run help

# Detect tools
DOCKER := $(shell command -v docker 2> /dev/null)

# ---------------------------------------------------------
# Help
# ---------------------------------------------------------

help:
	@echo ""
	@echo "Rust Project Commands:"
	@echo ""
	@echo "  make install      Install tools (pre-commit, etc.)"
	@echo "  make setup        Full project initialization"
	@echo "  make dev          Run in watch mode (requires cargo-watch)"
	@echo "  make build        Build binary in release mode"
	@echo "  make run          Build and run the project"
	@echo "  make test         Run all tests"
	@echo "  make lint         Run clippy for static analysis"
	@echo "  make format       Format code using rustfmt"
	@echo "  make check        Quick compilation check"
	@echo "  make clean        Remove target directory and artifacts"
	@echo "  make docker-build Build Docker image from $(DOCKER_FILE)"
	@echo "  make docker-run   Run the built Docker container"
	@echo "  make ci           Run all CI checks (fmt, clippy, test)"
	@echo ""

# ---------------------------------------------------------
# Core workflow
# ---------------------------------------------------------

install:
	@echo "Checking for Rust toolchain..."
	rustup show
	@echo "Installing common dev tools..."
	cargo install cargo-watch 2>/dev/null || echo "cargo-watch already installed"

setup: install
	@echo "Project setup complete."
	cp -n .env.example .env || true
	pre-commit install
	pre-commit install --hook-type commit-msg
	cargo fetch

dev:
	@echo "Starting development mode with hot-reload..."
	cargo watch -x run

build:
	@echo "Building release binary..."
	cargo build --release

run:
	@echo "Running application..."
	cargo run

test:
	@echo "Running tests..."
	cargo test

lint:
	@echo "Running Clippy..."
	cargo clippy -- -D warnings

format:
	@echo "Formatting code..."
	cargo fmt --all

check:
	@echo "Checking compilation..."
	cargo check

# ---------------------------------------------------------
# Docker
# ---------------------------------------------------------

docker-build:
ifneq ($(DOCKER),)
	@echo "Building Docker image..."
	docker build -f $(DOCKER_FILE) -t $(DOCKER_IMAGE) .
else
	@echo "Docker is not installed."
	@exit 1
endif

docker-run:
ifneq ($(DOCKER),)
	@echo "Running Docker container..."
	docker run --rm -it $(DOCKER_IMAGE)
else
	@echo "Docker is not installed."
	@exit 1
endif

# ---------------------------------------------------------
# Maintenance
# ---------------------------------------------------------

clean:
	@echo "Cleaning target directory..."
	cargo clean

ci: format lint test
	@echo "All CI checks passed locally."