import discord
from discord.ext import commands
import os

class babyinda(commands.Cog):
    def __init__ (self,bot):
        self.bot = bot
    @commands.command()
    async def babyinda(self,ctx):
        await ctx.send(file = discord.File("baby.png"))
def setup(bot):
    bot.add_cog(babyinda(bot))
        
        
    
