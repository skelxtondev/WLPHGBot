import discord
from discord.ext import commands
import os

class template(commands.Cog):
    def __init__ (self,bot):
        self.bot = bot
    @commands.command()
    async def template(self,ctx):
        #Code goes here
        pass
def setup(bot):
    bot.add_cog(template(bot))