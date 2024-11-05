from pydantic import Field
from pydantic_extra_types.color import Color
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: str = Field(default=...)
    embed_color: Color = Field(default="#7CB9E8")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", frozen=True)
