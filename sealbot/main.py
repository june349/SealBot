import logging
import sys

import discord
from pydantic import ValidationError

from sealbot.bot import SealBot
from sealbot.settings import Settings


def main():
    discord.utils.setup_logging()
    
    intents = discord.Intents.default()
    intents.message_content = True

    try:
        bot = SealBot(settings=Settings(), intents=intents)
        bot.run(bot.settings.token)
    except ValidationError as e:
        for err in e.errors():
            location = ".".join(map(str, err["loc"]))
            message = err["msg"]
            err_type = err["type"]
            logging.error(f"Settings validation error for '{location}': {message} ({err_type})")
        sys.exit(1)
    except discord.LoginFailure as e:
        logging.error(f"Login failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
