from Helpers import MetaInit, get_economy_symbol
from Services import add_balance, random_earnings
from discord.ext import commands
import discord

class WorkMeta(MetaInit):
    @commands.hybrid_command(name="work", description="Work to gain money")
    async def work_meta(self, ctx: commands.Context):
        guild_id = str(ctx.guild.id)
        earnings = random_earnings()
        add_balance(ctx.guild.id, ctx.author.id, earnings)
        MONEY_SYMBOL = get_economy_symbol(guild_id)
        embed = discord.Embed(
            title="Work ⛏️",
            description=f"`{ctx.author.display_name}` earned {MONEY_SYMBOL}{earnings} working. 💵",
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)