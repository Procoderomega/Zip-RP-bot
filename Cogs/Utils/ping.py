from discord.ext import commands
from discord import app_commands
from Helpers import MetaInit

class Ping_Meta(MetaInit):
    @commands.hybrid_command(name="ping", description="Returns 'pong' whit latency")
    async def ping_meta(self, ctx: commands.Context):
        lat = round(self.bot.latency * 1000)
        await ctx.send(f"Pong 🏓!\nLatency 🛜: {lat}ms")