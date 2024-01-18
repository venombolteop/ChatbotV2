import asyncio
import importlib

from pyrogram import idle

from Venom import LOGGER, VenomX
from Venom.modules import ALL_MODULES


async def anony_boot():
    try:
        await VenomX.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("Venom.modules." + all_module)

    LOGGER.info(f"@{VenomX.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping Venom Bot...")
