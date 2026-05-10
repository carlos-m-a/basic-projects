# -----------------------------
# Base image
# -----------------------------
FROM python:3.12-slim

# Evita bytecode y buffering raro en logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# -----------------------------
# Working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# System dependencies (si necesitas compilar algo)
# -----------------------------
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Install uv
# -----------------------------
RUN curl -Ls https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"

# -----------------------------
# Copy project files
# -----------------------------
COPY pyproject.toml uv.lock* /app/
COPY src /app/src

# -----------------------------
# Install dependencies
# -----------------------------
RUN uv sync --frozen --no-dev

# -----------------------------
# App execution
# -----------------------------
CMD ["uv", "run", "python", "src/app_name/main.py"]