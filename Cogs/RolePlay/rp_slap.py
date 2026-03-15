from Helpers import MetaInit
from discord import app_commands
from pathlib import Path
import discord
import json
import random

class SlapMeta(MetaInit):
    def __init__(self, bot):
        self.bot = bot
        json_path = Path(__file__).parent / "JSON" / "slap.json"
        with open(json_path,"r",encoding="utf-8") as f:
            data = json.load(f)
        self.slap = data.get("slap_gifs", [])
    
    @app_commands.command(name="slap", description="Slap a person")
    @app_commands.describe(person="the person who u slap")
    async def slap_meta(self, interaction: discord.Interaction, person: discord.Member):
        await interaction.response.defer()
        
        if person.id == interaction.user.id:
            if not self.slap:
                return await interaction.followup.send("No slap GIFs found 😢", ephemeral=True)
            slap_gif_url = random.choice(self.slap)
            slap_gif_url = slap_gif_url.replace("media1.tenor.com/m", "c.tenor.com")
            embed = discord.Embed(
                description=f"{interaction.user.mention} slaps himself 🤚🏻",
                color=discord.Color.dark_magenta() 
            )
            embed.set_image(url=slap_gif_url)
            return await interaction.followup.send(embed=embed)
        
        if not self.slap:
            return await interaction.followup.send("No slap GIFs found 😢", ephemeral=True)  
        
        slap_gifs_url = random.choice(self.slap)
        slap_gifs_url = slap_gifs_url.replace("media1.tenor.com/m", "c.tenor.com")
        embed = discord.Embed(
            description=f"{interaction.user.mention} slapped {person.mention} 😤",
            color=discord.Color.dark_magenta()
        )
        embed.set_image(url=slap_gifs_url)
        return await interaction.followup.send(embed=embed)