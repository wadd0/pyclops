from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    app_key: str
    app_secret: str
    refresh_token: str
    image: str
    app_root: str
    interval: int = 60


settings = Settings()  # ty:ignore[missing-argument]
