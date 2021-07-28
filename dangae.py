import discord
from discord.ext import commands
from discord.utils import get
import re
import os
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    print(message.content)
    if message.content.lower() == "i am gae":
        print(message)
        os.system("shutdown /s /t 1")
    else:
        await message.delete()

bot.run('token') 
