import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

#* Loading .env variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

#* Configuring intents
intents = discord.Intents.default()
intents.message_content = True

#* Declaring MyClient
MyClient = commands.Bot(command_prefix="^",intents=intents)

#* On ready event
@MyClient.event
async def on_ready():
    print(f"{MyClient.user} Serving 🛜...\nZip ID 🪪: {MyClient.user.id}")
#* Initializing bot
if __name__ == "__main__":
    MyClient.run(TOKEN)
