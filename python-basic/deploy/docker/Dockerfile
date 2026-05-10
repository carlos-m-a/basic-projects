# -----------------------------
# Base image
# -----------------------------
FROM python:3.12-slim

# Evita bytecode y buffering raro en logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT="/app/.venv" \
    PATH="/app/.venv/bin:$PATH"

# -----------------------------
# Working directory
# -----------------------------
WORKDIR /app
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# -----------------------------
# System dependencies (si necesitas compilar algo)
# -----------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# -----------------------------
# Copy & install
# -----------------------------
# 1. Configuration
COPY --chown=appuser:appgroup pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev --no-install-project
# 2. Source code
COPY --chown=appuser:appgroup src ./src
# 3. Sync, clean cache and set permissions
RUN uv sync --frozen --no-dev && \
    uv cache clean && \
    chown -R appuser:appgroup /app

# -----------------------------
# App execution
# -----------------------------
USER appuser
CMD ["python", "src/app_name/main.py"]