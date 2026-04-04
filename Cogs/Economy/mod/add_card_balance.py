
#! THIS IS A TESTING COMMAND
import discord
from discord import app_commands
from Services import add_balance_card
from Helpers import DEBUG, OK, MetaInit, get_economy_symbol

class AddBalanceToCardMeta(MetaInit):
    @app_commands.command(name="add_balanceto_card", description="Add balance to a card of an user")
    @app_commands.checks.has_permissions(administrator=True)
    async def add_balance_to_card_meta(self, interaction: discord.Interaction, target: discord.Member, amount: int):
        await interaction.response.defer()
        guild_id = int(interaction.guild.id)
        if not guild_id:
            return
        target_id = int(target.id)
        symbol = get_economy_symbol(guild_id)
        add_balance_card(guild_id,target_id,amount)
        embed = discord.Embed(
            description=f"{interaction.user.mention} added {symbol}{amount} to {target.mention} card 💳",
            color= discord.Color.purple()
        )
        await interaction.followup.send(embed=embed)