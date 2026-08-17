import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from Venom import VenomX
from Venom.database.chats import add_served_chat
from Venom.database.users import add_served_user
from Venom.modules.helpers import PNG_BTN


@VenomX.on_message(filters.command("ping") & ~filters.bot)
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="Pinging...",
    )
    try:
        await message.delete()
    except Exception:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=(
            f"\u0646\u064ey \u0628\u0627\u0628\u06cc!!\n"
            f"{VenomX.name} \u03b9\u03c3 \u0627\u0644\u06cc\u0641\u064e \U0001f940 "
            f"\u0627\u0646\u062f \u0648\u0648\u0631\u06a9\u06cc\u0646\u063a \u0641\u06cc\u0646\u064e "
            f"\u0648\u06cc\u062a\u0646 \u0627\u067e\u06cc\u0646\u06af \u0627\u0632\n"
            f"\u27e8 `{ms}` ms\n\n"
            f"<b>|| \u0645\u0627\u062f\u0647 \u0648\u06cc\u062a\u0646 \u2763\ufe0f "
            f"\u0628\u06cc\u0631 [\u06af\u06cc\u0646\u06af](https://t.me/{OWNER_USERNAME}) ||</b>"
        ),
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
