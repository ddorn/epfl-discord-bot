#!/bin/python
from discord import Intents, MemberCacheFlags

from src.constants import *
from src.core import CustomBot


def start():
    # We allow "! " to catch people that put a space in their commands.
    # It must be in first otherwise "!" always match first and the space is not recognised
    bot = CustomBot((PREFIX + " ", PREFIX), case_insensitive=True, owner_id=OWNER, intents=Intents.all())

    # We have our own help command, so remove the existing one before loading it
    bot.remove_command("help")

    # Load all cogs in File.COGS
    for cog in File.COGS.glob("*.py"):
        if cog.name.startswith("_"): continue
        bot.load_extension(cog.relative_to(File.TOP_LEVEL).as_posix().replace("/", ".")[:-3])
    bot.load_extension("src.errors")
    bot.load_extension("src.utils")
    bot.load_extension("src.constants")
    bot.load_extension("src.converters")

    # Let's goooo
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    start()
