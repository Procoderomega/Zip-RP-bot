
#~ PUBLIC
from .public.work import WorkMeta
from .public.wallet import WalletMeta
from .public.stealing import StealMeta
from .public.bank_card import BankCardMeta

#~ MODERATOR
from .mod.add_card_balance import AddBalanceToCardMeta
from .mod.del_balance import DeleteBalanceMeta
from .mod.add_balance import AddBalanceMeta
from .mod.show_balance import ShowBalanceMeta

#~ ADMINISTRATOR
from .admin.set_currency import EconomyConfigMeta


async def setup(bot):
    await bot.add_cog(WorkMeta(bot))
    await bot.add_cog(WalletMeta(bot))
    await bot.add_cog(EconomyConfigMeta(bot))
    await bot.add_cog(DeleteBalanceMeta(bot))
    await bot.add_cog(AddBalanceMeta(bot))
    await bot.add_cog(ShowBalanceMeta(bot))
    await bot.add_cog(StealMeta(bot))
    await bot.add_cog(BankCardMeta(bot))
    await bot.add_cog(AddBalanceToCardMeta(bot))