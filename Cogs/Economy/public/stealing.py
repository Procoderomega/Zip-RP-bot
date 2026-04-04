from discord import app_commands
import random
import discord
from Helpers import DEBUG, OK, MetaInit, get_economy_symbol
from Services import add_balance, remove_balance, get_balance

class StealMeta(MetaInit):
    @app_commands.command(name="steal", description="steal balance from an user")
    async def steal_meta(self, interaction: discord.Interaction, target: discord.Member):
        rand_steal = int(random.randint(50,500))
        guild_id = interaction.guild.id
        symbol = get_economy_symbol(guild_id)
        target_bal = get_balance(guild_id, target.id)
        if target_bal <= 0:
            embed = discord.Embed(
                description="User doesn't have balance 💵❌"
            )
            return await interaction.response.send_message(embed=embed)
        remove_balance(guild_id, target.id, rand_steal)
        add_balance(guild_id, interaction.user.id, rand_steal)
        msg = "All good."
        print(f"{msg:<45}{OK}")
        embed = discord.Embed(
            description=f"🚨 {interaction.user.mention} stealed `{symbol}`{rand_steal} from {target.mention} 🚨"
        )
        await interaction.response.send_message(embed=embed)
        