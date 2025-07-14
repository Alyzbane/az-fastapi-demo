from fastapi.security import APIKeyHeader
from fastapi import HTTPException, status, Security

from loguru import logger
from src.configs.settings import get_settings

# Initialize settings to load API keys from environment
settings = get_settings()
api_key_header = APIKeyHeader(name="X-API-Key")

# Security dependency to check API key
def auth_api_key(api_key: str = Security(api_key_header)):
    if api_key not in settings.api_keys:
        logger.error("Invalid API Key provided")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key",
        )

if __name__ == "__main__":
    # Example usage of the auth_api_key function
    try:
        logger.debug(f"Authenticating API Key")
        auth_api_key("abc123")
    except HTTPException as e:
        logger.error(f"Authentication failed: {e.detail}")
    else:
        logger.info("Authentication successful")