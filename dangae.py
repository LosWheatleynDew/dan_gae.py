import discord
from discord.ext import commands
from discord.utils import get
import re
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author == client.user: #Ignore own messages
        return
    
    print(message.content)
    if message.content.lower() == "i am gae": 
        print(message)
    else:
        await message.delete()
        await message.channel.send("https://cdn.discordapp.com/attachments/829794542071840823/870262564259504199/proof.jpg") #send proof that dan gae

bot.run('token') 
