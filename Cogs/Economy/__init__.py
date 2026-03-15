from .work import WorkMeta
from .wallet import WalletMeta
from .set_currency import EconomyConfigMeta
from .del_balance import DeleteBalanceMeta

async def setup(bot):
    await bot.add_cog(WorkMeta(bot))
    await bot.add_cog(WalletMeta(bot))
    await bot.add_cog(EconomyConfigMeta(bot))
    await bot.add_cog(DeleteBalanceMeta(bot))