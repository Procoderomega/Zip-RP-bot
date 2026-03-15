from Helpers import MetaInit
from discord import app_commands
from pathlib import Path
import json
import random
import discord

class HugMeta(MetaInit):
    def __init__(self, bot):
        self.bot = bot
        json_path = Path(__file__).parent / "JSON" / "hug.json"
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.hug = data.get("hug_gifs", [])
        self.self_hug = data.get("self_hug_gifs", [])

    @app_commands.command(name="hug", description="Send a hug GIF to someone")
    @app_commands.describe(person="Person to hug")
    async def hug_meta(self, interaction: discord.Interaction, person: discord.Member):
        await interaction.response.defer()
        if person.id == interaction.user.id:
            if not self.self_hug:
                return await interaction.followup.send("No self-hug GIFs found 😢", ephemeral=True)
            gif_url = random.choice(self.self_hug)
            embed = discord.Embed(
                description=f"{interaction.user.mention} hugs himself 🫂",
                color=discord.Color.pink()
            )
            embed.set_image(url=gif_url)
            return await interaction.followup.send(embed=embed)
        
        if not self.hug:
            return await interaction.followup.send("No hug GIFs found 😢", ephemeral=True)
        
        gif_url = random.choice(self.hug)
        embed = discord.Embed(
            description=f"{interaction.user.mention} hugs {person.mention} 🫂",
            color=discord.Color.purple()
        )
        embed.set_image(url=gif_url)
        await interaction.followup.send(embed=embed)
