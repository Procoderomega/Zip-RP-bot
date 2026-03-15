from colorama import Fore, Style, init
from discord.ext import commands
from dotenv import load_dotenv
from Configs import bot_config
import os
import discord

# Loading .env variables
load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = bot_config["General"]["Prefix"]

# Configuring intents
intents = discord.Intents.default()
intents.message_content = True

# Declaring MyClient
class MyBot(commands.Bot):
    async def setup_hook(self):
        # Loading da cogs
        cogs = ["Utils cogs","Economy cogs","RolePlay cogs","Sync slash cog"] #! Mod and Fun cogs are not ready to be loaded yet
        #// await self.load_extension("Cogs.Moderation")
        #// await self.load_extension("Cogs.Fun")
        await self.load_extension("Cogs.Economy")
        await self.load_extension("Cogs.Utils")
        await self.load_extension("Cogs.RolePlay")
        await self.load_extension("Helpers.sync_slash")
        for cog in cogs:
            print(f"{cog:<18}[{Fore.GREEN}OK{Style.RESET_ALL}]")
MyClient = MyBot(command_prefix=PREFIX, intents=intents, help_command=None)

# On ready event
@MyClient.event
async def on_ready():
    activity = discord.Streaming(name="Fundamental Paper Education",url="https://www.youtube.com/watch?v=0x7zdgK-FFU",platform="YouTube")
    await MyClient.change_presence(activity=activity)
    print(f"{MyClient.user} Serving 🛜...\nZip ID 🪪: {MyClient.user.id}\nStreaming success ✅.")
# Initializing bot
if __name__ == "__main__":
    MyClient.run(TOKEN)