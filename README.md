# ML FastAPI Sentiment Analysis API

A FastAPI application that provides sentiment analysis using a pre-trained RoBERTa model from Hugging Face. Analyzes text inputs and returns sentiment scores (negative, neutral, positive).

## Features

- Sentiment analysis using Cardiff NLP's Twitter RoBERTa model
- Batch processing for multiple text inputs
- API key authentication
- Dockerized deployment with multi-stage builds
- Health monitoring endpoint

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended package manager)
- Docker & Docker Compose (for containerized deployment)

## Installation

### Local Development

```bash
# Clone and setup
git clone <repository-url>
cd ml-fastapi-observation
cp .env.example .env

# Install dependencies (recommended)
uv sync

# Or with pip
pip install -r requirements.txt

# Run application
uv run uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload
```

### Docker Deployment

```bash
docker-compose up --build
```

## Configuration

Create a `.env` file:
```env
API_KEYS=["your-api-key-1", "your-api-key-2"]
```

## API Documentation

**Base URL:** `http://localhost:8001`
**API Docs:** `http://localhost:8001/docs` (Swagger UI)

### Authentication
All endpoints require an API key header:
```
X-API-Key: your-api-key-here
```

### Endpoints

**Health Check:**
```bash
curl http://localhost:8001/health
```

**Sentiment Analysis:**
```bash
curl -X POST "http://localhost:8001/v1/classification/score/" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: abc123" \
  -d '{"input_text_list": ["I love this!", "This sucks", "It is okay"]}'
```

**Response:**
```json
{
  "output": {
    "I love this!": {"negative": 0.01, "neutral": 0.01, "positive": 0.98},
    "This sucks": {"negative": 0.96, "neutral": 0.02, "positive": 0.02},
    "It is okay": {"negative": 0.15, "neutral": 0.75, "positive": 0.10}
  }
}
```

## Project Structure

```
ml-fastapi-observation/
├── src/
│   ├── main.py                 # FastAPI application
│   ├── setup_model.py          # Model setup
│   ├── security.py             # Authentication
│   ├── api/v1/                 # API routes
│   └── configs/                # Settings & logging
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

## Model Information

- **Model:** `cardiffnlp/twitter-roberta-base-sentiment`
- **Labels:** negative (0), neutral (1), positive (2)
- **Preprocessing:** Automatic text cleaning (usernames → @user, URLs → http)

## Development

```bash
# Install with dev dependencies
uv sync --dev

# Run with auto-reload
uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8001

# Access docs
open http://localhost:8001/docs
```

## Testing

```python
import requests

response = requests.post(
    "http://localhost:8001/v1/classification/score/",
    headers={"X-API-Key": "abc123", "Content-Type": "application/json"},
    json={"input_text_list": ["Great product!", "Terrible service"]}
)
print(response.json())
```

## License
This project is licensed under the GNU GPL v3.0. See the [LICENSE](LICENSE) file for details.