from discord import Intents
from discord.ext import commands

from sealbot.settings import Settings


class SealBot(commands.Bot):
    def __init__(self, settings: Settings, intents: Intents):
        super().__init__(
            intents=intents,
            command_prefix=settings.prefix, 
            description="A Discord bot centered around seals :3"
        )
        self.settings = settings
