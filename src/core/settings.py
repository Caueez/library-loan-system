from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict, BaseSettings


class DatabaseSettings(BaseModel):
    type: str
    uri: str


class Settings(BaseSettings):
    database: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_nested_delimiter="__",
        )
        