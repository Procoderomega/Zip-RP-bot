from discord.ext import commands
from pathlib import Path
import tomllib  # solo para leer
import tomli_w  # para escribir

CONFIG_PATH = Path(__file__).parent.parent.parent / "Configs" / "config.toml"

class EconomyConfigMeta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="set_economy_symbol", description="Set the economy symbol")
    async def set_economy_symbol_meta(self, ctx: commands.Context, symbol: str):
        # Leer config con tomllib
        with open(CONFIG_PATH, "rb") as f:
            config = tomllib.load(f)

        # Validar longitud del símbolo
        if len(symbol) > 2:
            await ctx.send("❌ Symbol too long! Use 1 or 2 characters max.")
            return

        # Actualizar símbolo
        config["Economy"]["Economy_Symbol"] = symbol

        # Guardar cambios con tomli-w
        with open(CONFIG_PATH, "wb") as f:
            tomli_w.dump(config, f)

        await ctx.send(f"✅ Economy symbol updated to: {symbol}", ephemeral= True)
        
        print("All good")