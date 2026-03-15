from .work import WorkMeta
from .wallet import WalletMeta
from .set_currency import EconomyConfigMeta

async def setup(bot):
    await bot.add_cog(WorkMeta(bot))
    await bot.add_cog(WalletMeta(bot))
    await bot.add_cog(EconomyConfigMeta(bot))