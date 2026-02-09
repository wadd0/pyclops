"""Settings module to load configuration from .env file using Pydantic Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Pydantic settings class to load configuration."""

    model_config = SettingsConfigDict(env_file=".env")
    app_key: str
    app_secret: str
    refresh_token: str
    image: str
    app_root: str
    interval: int = 60


settings = Settings()  # ty:ignore[missing-argument]
