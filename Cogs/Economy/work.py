from Helpers import MetaInit, get_economy_symbol
from Services import add_balance, random_earnings
from discord import app_commands
from discord.ext import commands
import discord

class WorkMeta(MetaInit):
    @commands.hybrid_command(name="work", description="Work to gain money")
    async def work_meta(self, ctx: commands.Context):
        earnings = random_earnings()
        add_balance(ctx.author.id, earnings)
        MONEY_SYMBOL = get_economy_symbol()
        embed = discord.Embed(
            title="Work ⛏️",
            description=f"`{ctx.author.display_name}` earned {MONEY_SYMBOL}{earnings} working. 💵",
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)