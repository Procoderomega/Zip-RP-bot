from Helpers import MetaInit
from pathlib import Path
from discord import app_commands
import json
import random
import discord

class KissMeta(MetaInit):
    def __init__(self, bot):
        self.bot = bot
        json_path = Path(__file__).parent / "JSON" / "kiss.json"
        with open(json_path,"r",encoding="utf-8") as f:
            data = json.load(f)
        self.kiss = data.get("kiss_gifs", [])
    
    @app_commands.command(name="kiss", description="Kiss your beloved person")
    @app_commands.describe(person="Person to kiss")
    async def kiss_meta(self, interaction: discord.Interaction, person: discord.Member):
        await interaction.response.defer()
        
        if person.id == interaction.user.id:
            if not self.kiss:
                return await interaction.followup.send("No kiss GIFs found 😢", ephemeral=True)
            kiss_gifs_url = random.choice(self.kiss)
            embed = discord.Embed(
                description=f"{interaction.user.mention} kisses himself 💘",
                color=discord.Color.purple()
            )
            embed.set_image(url=kiss_gifs_url)
            return await interaction.followup.send(embed=embed)
        
        if not self.kiss:
            return await interaction.followup.send("No kiss GIFs found 😢", ephemeral=True)
        
        kiss_gif_url = random.choice(self.kiss)
        embed = discord.Embed(
            description=f"{interaction.user.mention} kisses {person.mention}",
            color=discord.Color.purple()
        )
        embed.set_image(url=kiss_gif_url)
        return await interaction.followup.send(embed=embed)