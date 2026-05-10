# -----------------------------
# Stage 1: Build
# -----------------------------
FROM node:20-slim AS builder

# Set working directory
WORKDIR /app

# Install system dependencies for native module compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency manifests
COPY package.json package-lock.json* ./

# Install all dependencies (including devDependencies for compilation)
RUN npm ci

# Copy source code and TS configuration
COPY tsconfig.json ./
COPY src ./src

# Compile TypeScript to JavaScript (generates /dist folder)
RUN npm run build

# -----------------------------
# Stage 2: Runtime
# -----------------------------
FROM node:20-slim AS runner

# Production environment variables
ENV NODE_ENV=production \
    PORT=3000

WORKDIR /app

# Security: Create a system user and group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Copy only necessary artifacts from the builder stage
# 1. The compiled JavaScript code
COPY --from=builder --chown=appuser:appgroup /app/dist ./dist
# 2. Manifest files for production dependency installation
COPY --from=builder --chown=appuser:appgroup /app/package.json ./package.json
COPY --from=builder --chown=appuser:appgroup /app/package-lock.json ./package-lock.json

# Install production dependencies only and clean cache
RUN npm ci --omit=dev && \
    npm cache clean --force && \
    chown -R appuser:appgroup /app

# -----------------------------
# App execution
# -----------------------------
USER appuser

# Document the port the app listens on
EXPOSE 3000

# Run the transpiled code from the dist folder
CMD ["node", "dist/index.js"]