from discord import app_commands
from Helpers import MetaInit, get_economy_symbol
from Services import get_balance_card
import discord

class BankCardMeta(MetaInit):
    @app_commands.command(name="bank",description="Check your bank balance")
    async def create_bank_card_meta(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        guild_id = interaction.guild.id
        if not guild_id:
            return
        symbol = get_economy_symbol(guild_id)
        user_id = interaction.user.id
        balance = get_balance_card(guild_id, user_id)
        if balance == None:
            embed = discord.Embed(
                description=f"{interaction.user.mention} You dont have balance in your card, Work! 💳",
                color= discord.Color.purple()
            )
            return await interaction.followup.send(embed=embed, ephemeral=True)
        embed = discord.Embed(
            description=f"{interaction.user.mention} Your bank balance is: `{symbol}`{balance}",
            color= discord.Color.purple()
        )
        await interaction.followup.send(embed=embed, ephemeral=True)