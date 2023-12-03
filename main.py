import settings
import logging
import discord
from discord.ext import commands
from datetime import datetime, timedelta, timezone

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="*", intents=intents)
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command()
    async def ping(ctx):
        await ctx.send("Wiktor super gość")
    
    @bot.command()
    async def joined(ctx, user : discord.Member):
        joined_time = str(user.joined_at)
        joined_time = joined_time[:-6]
        current_time = str(datetime.utcnow())
        current_time = current_time[:-1]
        #diff = current_time - joined_time
        '''
        difference = current_time - joined_time
        days, seconds = divmod(difference.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        duration = f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)}, seconds"
        '''
        await ctx.send(f"User joined: {str(joined_time)}\nNow is: {current_time}")


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()