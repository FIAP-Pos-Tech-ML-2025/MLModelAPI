from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "mlmodel-api"
    ENVIRONMENT: str = "dev"
    LOG_LEVEL: str = "INFO"

    AML_ENDPOINT: str
    AML_AUTH_TYPE: str = "key"
    AML_API_KEY: str | None = None
    KEYVAULT_URI: str | None = None
    SECRET_NAME: str | None = None

    APPINSIGHTS_CONNECTION_STRING: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()