import settings
import logging
import discord
from discord.ext import commands
from datetime import datetime, timedelta, timezone
from cogs.commands import Commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="*", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        await bot.load_extension("cogs.commands")

        # for cmd_file in settings.CMDS_DIR.glob("*.py"):
        #     if cmd_file.name != "__init__.py":
        #         await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

        # for cog_file in settings.COGS_DIR.glob("*.py"):
        #     if cog_file.name != "__init__.py":
        #         await bot.load_extension(f"cogs.{cog_file.name[:-3]}")
    
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error")
        
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()