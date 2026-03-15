from discord.ext import commands
from Helpers import MetaInit, get_economy_symbol
from Services import get_balance
from pathlib import Path
from Configs import bot_config
import discord

class WalletMeta(MetaInit):
    @commands.hybrid_command(name="wallet", description="See your current balance")
    async def wallet_meta(self, ctx: commands.Context):
        current_balance = get_balance(ctx.author.id)
        MONEY_SYMBOL = get_economy_symbol()
        embed = discord.Embed(
            title="Wallet 💵",
            description=f"{ctx.author.mention} your wallet currently has `{MONEY_SYMBOL}`{current_balance} 💵 !",
            color=discord.Color.purple()
        )
        #//file_path = Path(__file__).parent.parent.parent / "Assets" / "Images" / "coin-removebg-preview.png"
        #//file = discord.File(file_path, filename="coin.png")
        #//embed.set_footer(icon_url="attachment://coin.png")
        #! Unfinished/broken lines
        return await ctx.send(embed=embed)