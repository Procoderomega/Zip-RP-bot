from .ping import Ping_Meta

async def setup(bot):
    await bot.add_cog(Ping_Meta(bot))