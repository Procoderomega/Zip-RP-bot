from Helpers import MetaInit
from discord.ext import commands
from discord import app_commands
from Services import delete_balance
from Helpers import DEBUG
import discord

class DeleteBalanceMeta(MetaInit):
    @commands.hybrid_command(name="delete_user_balance", description="sets specific user balance to 0")
    @commands.has_permissions(administrator=True)
    @app_commands.default_permissions(administrator=True)
    async def delete_balance_absolute(self, ctx: commands.Context, member: discord.Member):
        guild_id = str(ctx.guild.id)
        user_id = str(member.id)
        
        delete_balance(guild_id, user_id)
        
        embed = discord.Embed(
            description=f"{member.display_name} balance was reset to 0 ✅",
            color=discord.Color.dark_magenta()
        )
        msg = "deleted user balance correctly"
        print(f"{msg:<45}{DEBUG}")
        return await ctx.send(embed=embed, ephemeral=True)