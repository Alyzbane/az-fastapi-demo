# === Stage 1: Builder ===
FROM python:3.10-slim AS builder

WORKDIR /app
COPY requirements.txt .

# Install build tools temporarily
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc g++ build-essential \
        && pip install --no-cache-dir -r requirements.txt \
        && apt-get purge -y --auto-remove gcc g++ build-essential \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

COPY ./src /app/src
RUN mkdir /pretrained

ENV PYTHONPATH=/app

# Download the model during build (model files will be kept)
RUN ["python", "-m", "src.setup_model"]

# === Stage 2: Final image ===
FROM python:3.10-slim

WORKDIR /app

# Copy installed site-packages from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy your app code and model weights
COPY --from=builder /app /app
COPY --from=builder /pretrained /pretrained

EXPOSE 8001

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]