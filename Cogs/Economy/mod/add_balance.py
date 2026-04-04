from discord.ext import commands
from Helpers import MetaInit
from discord import app_commands
from Services import add_balance
from Helpers import get_economy_symbol
import discord

class AddBalanceMeta(MetaInit):
    @commands.hybrid_command(name="add_balance", description="Add balance to an user")
    @commands.has_permissions(administrator=True)
    @app_commands.default_permissions(administrator=True)
    async def add_balance_meta(self, ctx: commands.Context, member: discord.Member, amount: int):
        guild_id = str(ctx.guild.id)
        symbol = get_economy_symbol(guild_id)
        add_balance(guild_id, member.id, amount)
        
        embed = discord.Embed(
            description=f"{ctx.author.display_name} added {symbol}{amount} to {member.display_name}",
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)