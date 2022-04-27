import discord
from discord.ext import commands
#You need to create the webserver file
from webserver import keep_alive
import os

 
client = commands.Bot(command_prefix="+", self_bot=True , help_command = None)
client.remove_command('help')


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="give me a star"))
  print("login")

  

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN , bot=False)
