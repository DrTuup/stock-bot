from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    schedule: str = "0 0 * * *"


# Singleton instance of the settings
settings = Settings()
