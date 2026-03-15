from discord import app_commands
from pathlib import Path
from Helpers import MetaInit
import discord
import json

class CharPatMeta(MetaInit):
    def __init__(self, bot):
        self.bot = bot
        json_path = Path(__file__).parent / "JSON" / "characters_pat.json"
        with open(json_path,"r",encoding="utf-8") as f:
            data = json.load(f)
        #? Getting characters dict
        self.characters = data.get("characters_gifs", {})
        self.estudents = self.characters.get("estudiantes", {})
        self.teachers = self.characters.get("maestros", {})

    @app_commands.command(name="pat_student")
    @app_commands.describe(character="Character who you pat")
    @app_commands.choices(character=[
        app_commands.Choice(name="Zip", value="zip"),
        app_commands.Choice(name="Edward", value="edward"),
        app_commands.Choice(name="Oliver", value="oliver"),
        app_commands.Choice(name="Human Oliver", value="human_oliver"),
        app_commands.Choice(name="Petunia", value="petunia"),
        app_commands.Choice(name="Skell", value="skell"),
        app_commands.Choice(name="Claire", value="claire"),
        app_commands.Choice(name="Kevin", value="kevin"),
        app_commands.Choice(name="Cubbie", value="cubbie"),
        app_commands.Choice(name="Riley", value="riley"),
        app_commands.Choice(name="Abbie", value="abbie"),
        app_commands.Choice(name="Engel", value="engel"),
        app_commands.Choice(name="Lizzy", value="lizzy"),
        app_commands.Choice(name="Alice", value="alice"),
        app_commands.Choice(name="Mad Alice", value="mad_alice"),
    ])
    async def estudent_pat_meta(self, interaction: discord.Interaction, character: app_commands.Choice[str]):
        await interaction.response.defer()
        
        if not self.characters:
            return await interaction.followup.send("No FPE characters GIFs found 😢", ephemeral=True)
        
        gif_char = self.estudents.get(character.value)
        embed = discord.Embed(
            description=f"{interaction.user.mention} pats {character.name}",
            color=discord.Color.purple()
        )
        embed.set_image(url=gif_char)
        await interaction.followup.send(embed=embed)
    
    @app_commands.command(name="pat_teacher")
    @app_commands.describe(character="Character you pat")
    @app_commands.choices(character=[
        app_commands.Choice(name="Miss Thavel", value="miss_thavel"),
        app_commands.Choice(name="Miss Circle", value="miss_circle"),
        app_commands.Choice(name="Miss Blomie", value="miss_blomie"),
        app_commands.Choice(name="Miss Sasha", value="miss_sasha"),
        app_commands.Choice(name="Miss Emily", value="miss_emily"),
        app_commands.Choice(name="Mister Demi", value="mister_demi"),
        app_commands.Choice(name="Miss Grace", value="miss_grace")
    ])
    async def teacher_pat_meta(self, interaction: discord.Interaction, character: app_commands.Choice[str]):
        await interaction.response.defer()
        if not self.characters:
            return await interaction.followup.send("No FPE characters GIFs found 😢", ephemeral=True)
        
        gif_char = self.teachers.get(character.value)
        embed = discord.Embed(
            description=f"{interaction.user.mention} pats {character.name}",
            color=discord.Color.purple()
        )
        embed.set_image(url=gif_char)
        return await interaction.followup.send(embed=embed)