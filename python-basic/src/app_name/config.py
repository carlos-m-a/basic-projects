from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Define variables with their types and default values
    PROJECT_NAME: str = "App Name"
    DATABASE_URL: str
    API_KEY: str | None = None
    DEBUG: bool = False

    # Configuration to read the .env file automatically
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Ignore variables in .env that are not defined here
    )

# Instantiate once to be used across the entire app (Singleton)
settings = Settings()