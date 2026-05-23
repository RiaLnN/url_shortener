from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    BASE_URL: str = ""
    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        env_file_encoding="utf-8",
    )

settings = AppSettings()