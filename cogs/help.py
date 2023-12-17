import discord
from discord.ext import commands
import settings

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def helpJerry(self, ctx):
        help_embed = discord.Embed(title="Command list:", description="Remember to use '*' prefix before every command", color=discord.Color.random())
        help_embed.set_author(name="JerryBot", icon_url=self.bot.user.avatar)
        help_embed.add_field(name="help", value="Shows commands and its categories", inline=False)
        help_embed.add_field(name="joined", value="Shows how long a user is on this server\njoined <user>", inline=False)
        help_embed.add_field(name="myInfo", value="Short history about this bot", inline=False)
        help_embed.set_footer(text=f"Requested by <@{ctx.author}>", icon_url=ctx.author.avatar)
        await ctx.send(embed=help_embed)

    @commands.command()
    async def myInfo(self, ctx):
        await ctx.send(f"I am just simple discord bot ready to help you if you need it\nI was created by {settings.AUTHOR_NAME} to help him learn new things and entertain his friends\nCheck my command list by typing *helpJerry")
        

async def setup(bot):
    await bot.add_cog(Help(bot))