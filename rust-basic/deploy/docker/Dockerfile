# --- Build Stage ---
FROM rust:1.75-slim AS builder

WORKDIR /usr/src/app

# Copy configuration files from the root
COPY Cargo.toml Cargo.lock ./

# Dependency caching trick
RUN mkdir src && echo "fn main() {}" > src/main.rs
RUN cargo build --release

# Copy the actual source code from the root
COPY src ./src

# Ensure the real source is compiled
RUN touch src/main.rs && cargo build --release

# --- Execution Stage ---
FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the binary from the builder stage
# Replace "your_binary_name" with the actual name in Cargo.toml
COPY --from=builder /usr/src/app/target/release/your_binary_name /app/rust_app

CMD ["./rust_app"]