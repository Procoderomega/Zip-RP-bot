from Services import get_balance
from Helpers import MetaInit, DEBUG,OK,FAIL, get_economy_symbol
from discord.ext import commands
from discord import app_commands
import discord

class ShowBalanceMeta(MetaInit):
    @app_commands.command(name="show_user_balance", description="Shows balance from user")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.default_permissions(administrator=True)
    async def show_balance_meta(self, interaction: discord.Interaction, member: discord.Member, invisible: bool = True):
        await interaction.response.defer(ephemeral=invisible)
        guild_id = str(interaction.guild.id)
        user_id = str(member.id)
        symbol = get_economy_symbol(guild_id)
        balance = get_balance(guild_id, user_id)
        
        if balance is None:
            embed = discord.Embed(
                description=f"{member.display_name} No DB record found",
                color=discord.Color.red()
            )
            msg = f"Tried to show balance of {member.display_name}, but no DB record found"
            print(f"{msg:<45}{DEBUG}->{FAIL}")
            return await interaction.followup.send(embed=embed, ephemeral=invisible)
        
        embed = discord.Embed(
            description=f"{member.display_name} currently has {symbol}{balance} 💵",
            color=discord.Color.purple()
        )
        msg = "Succesfully showed user balance"
        print(f"{msg:<45}{DEBUG}->{OK}")
        return await interaction.followup.send(embed=embed, ephemeral=invisible)