'''
import discord
import datetime as dt

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, ctx, user: discord.Member):
        joined_day = user.joined_at
        today_is = dt.datetime.now()
        duration = (today_is - joined_day).days

        await ctx.send(f"User joined: {joined_day}\nNow is: {today_is}\nWhich means {duration} days passed from this day")

def setup(bot):
    bot.add_cog(Commands(bot))
'''