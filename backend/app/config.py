from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BRIGHTDATA_API_TOKEN: str = ""
    BRIGHTDATA_COLLECTOR_ID: str = ""
    BRIGHTDATA_TARGET_URL: str = "https://www.smartprix.com/laptops"
    DATABASE_URL: str = "postgresql+asyncpg://webscout:webscout@localhost:5432/webscout"
    LLM_API_KEY: str = ""
    LLM_MODEL: str = "gemini-2.5-flash"
    DEMO_MODE: bool = False
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    FRONTEND_URL: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

def get_settings() -> Settings:
    return Settings()
