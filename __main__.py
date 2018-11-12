import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.client
client = commands.Bot(command_prefix = "!")

# Message to tell you when the bot is ready
@client.event
async def on_ready() :
     print("Bot is Ready!")


# Normal Text Chat
@client.event
async def on_message(message) :
     if message.content.upper() == ("HI") :
         await client.send_message(message.channel, "Hello There!")
     if message.content.upper() == ("ARE YOU OK?") :
         await client.send_message(message.channel, "Yup, I'm great thanks :)")
		 
# Bot Commands
     if message.content.upper().startswith('!H') :
          userID = message.author.id
          await client.send_message(message.channel, "<@%s> Hello There!" % (userID))
     if message.content.upper().startswith('!S') :

          args = message.content.split(" ")
          args[1:] = ("Hey There")
          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))



# Client Secret API Key
client.run("***************************************************")
