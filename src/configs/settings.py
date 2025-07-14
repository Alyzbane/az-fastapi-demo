from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_keys: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings() -> Settings:
    """
    Returns an instance of Settings with API keys loaded from the environment.
    """
    return Settings()