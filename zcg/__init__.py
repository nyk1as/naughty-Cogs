from redbot.core.bot import Red
from redbot.core.utils import get_end_user_data_statement

from .zcg import ZCG

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)


async def setup(bot: Red) -> None:
    cog = ZCG(bot)
    await bot.add_cog(cog)
