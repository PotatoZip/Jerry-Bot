import discord
from discord.ext import commands
import datetime as dt

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Wiktor super gość")
        
    @commands.command()
    async def joined(self, ctx, user: discord.Member):
        current_day = (dt.datetime.utcnow()).day
        current_month = (dt.datetime.utcnow()).month
        current_year = (dt.datetime.utcnow()).year

        joined_day = (user.joined_at).day
        joined_month = (user.joined_at).month
        joined_year = (user.joined_at).year
        
        days = current_day - joined_day
        months = current_month - joined_month
        years = current_year - joined_year
        if current_day < joined_day:
            days %= 30
            months -= 1
        if current_month < joined_month:
            days %= 12
            years -= 1

        joined_time = str(user.joined_at)[:-13]
        await ctx.send(f"This user is with us:\n{days} days, {months} months, {years} years\nJoined date: {joined_time}\n")

async def setup(bot):
    await bot.add_cog(Commands(bot))