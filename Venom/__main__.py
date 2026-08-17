import asyncio
import importlib

from pyrogram import idle

from Venom import LOGGER, VenomX
from Venom.database import init_indexes, close_db
from Venom.modules import ALL_MODULES


async def main():
    try:
        await VenomX.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    try:
        await init_indexes()
    except Exception as ex:
        LOGGER.error(f"Index initialization failed: {ex}")

    for all_module in ALL_MODULES:
        importlib.import_module("Venom.modules." + all_module)

    LOGGER.info(f"@{VenomX.username} Started.")
    await idle()
    LOGGER.info("Shutting down Venom Bot...")
    await VenomX.stop()
    await close_db()


if __name__ == "__main__":
    asyncio.run(main())
