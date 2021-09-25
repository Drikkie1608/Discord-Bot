import os
from discord.ext import commands
import discord
from keep_alive import keep_alive

from dotenv import load_dotenv
load_dotenv()

import time

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# loading all cogs
for filename in os.listdir("./extensions"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'extensions.{filename[:-3]}')

# bot is online
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# keep_alive() # only use on repl.it
bot.run(os.getenv('BOT_TOKEN'))