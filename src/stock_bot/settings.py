from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    avatar_url: str = (
        "https://cdn.jim-nielsen.com/ios/512/stocks-2025-08-05.png?rf=1024"
    )
    stock: str = "VWCE.DE"
    discord_webhook_url: str = ""


settings = Settings()
