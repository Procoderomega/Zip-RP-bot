from discord.ext import commands
from pathlib import Path
import json

CONFIG_PATH = Path(__file__).parent.parent.parent / "Configs" / "json" / "economy_general_configs.json"

class EconomyConfigMeta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="set_economy_symbol", description="Set the economy symbol")
    async def set_economy_symbol_meta(self, ctx: commands.Context, symbol: str):
        guild_id = str(ctx.guild.id)
        
        with open(CONFIG_PATH, "rb") as f:
            config = json.load(f)
            
        if len(symbol) > 2:
            return await ctx.send("❌ Symbol too long! Use 1 or 2 characters max.")
        if guild_id not in config["guilds"]:
            config["guilds"][guild_id] = {}
        # Actualizar símbolo
        config["guilds"][guild_id]["symbol"] = symbol

        # Guardar cambios con tomli-w
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=4)

        await ctx.send(f"✅ Economy symbol updated to: {symbol}", ephemeral= True)
        
        print("All good")