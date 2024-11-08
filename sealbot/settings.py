from pydantic import Field, DirectoryPath
from pydantic_extra_types.color import Color
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: str = Field(default=...)
    prefix: str = Field(default="+", min_length=1, max_length=1)
    assets_dir: DirectoryPath = Field(default=...)
    embed_color: Color = Field(default="#7CB9E8")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", frozen=True)
