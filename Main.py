import discord
from discord.ext import commands, tasks
import os

#Cogs are loaded with the given code inside them that run a command or event this improves effiency and overall matainibility, I have left a template to make it easier to produce new commands

#Whenever a major change is made make sure to commit it to the github 

# Documentation is here https://discordpy.readthedocs.io/en/stable/

#Discord Bot token should be kept safe at all times
token = ("NzUyNjAwMTQ5ODEyODM4NTcy.X1Z_gg.D_WxVDffHvzHOi8MXZnX4dGWz3Y")

#Prefix to call for commands
prefix = ('!')

#Assigning to make it easier to call for bot activities
bot = commands.Bot(command_prefix=prefix)

@bot.command()
async def loadcog(ctx, cog):
    bot.load_entension(f"cogs.{cog}")
@bot.command()
async def unloadcog(ctx, cog):
    bot.unload_entension(f"cogs.{cog}")
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
@bot.event
async def on_ready():
    print("Bot is online")
bot.run(token)
