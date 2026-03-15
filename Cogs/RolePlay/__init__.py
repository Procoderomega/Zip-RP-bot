from .rp_hug import HugMeta
from .rp_kiss import KissMeta
from .rp_slap import SlapMeta
from .character_pat import CharPatMeta

async def setup(bot):
    await bot.add_cog(HugMeta(bot))
    await bot.add_cog(KissMeta(bot))
    await bot.add_cog(SlapMeta(bot))
    await bot.add_cog(CharPatMeta(bot))