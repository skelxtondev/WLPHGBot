import discord
from discord.ext import commands
import os

class independence(commands.Cog):
    def __init__ (self,bot):
        self.bot = bot
    @commands.command()
    async def independence(self,ctx):
        await ctx.send(file = discord.File("independence.txt"))
def setup(bot):
    bot.add_cog(independence(bot))
        
