import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from Venom import VenomX
from Venom.database.chats import add_served_chat
from Venom.database.users import add_served_user
from Venom.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@VenomX.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("Work with ✦ Sahab..")
        await asyncio.sleep(0.2)
        await accha.edit("Work with ✦ Sahab.....")
        await asyncio.sleep(0.2)
        await accha.edit("Work with ✦ Sahab..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**\u06f5 \u0647\u064a, \u0627\u0646\u0627 \u0627\u0645 {VenomX.name}**\n**\u2773 \u0627\u0646 \u0622\u06cc \u0628\u0627\u0633\u062a \u06f1 \u0686\u0627\u062a\u0628\u0648\u062a.**\n**\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501**\n**\u2773 \u0648\u0633\u0627\u063a\u0629 /chatbot [\u0645\u0637\u0641\u064a/\u0645\u0639\u0627\u0637\u0641]**\n<b>||\u06f5 \u0647\u06cc\u062a \u0647\u0644\u067e \u0628\u062a\u0646 \u0628\u0631\u0627\u06cc \u06a9\u0645\u06a9||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@VenomX.on_message(filters.command("help") & ~filters.bot)
async def help_cmd(client, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**\u0647\u064a, \u067e\u0645 \u0645\u0646\u0628\u0631\u0627 \u0628\u0631\u0627\u06cc \u06a9\u0645\u06a9 \u06a9\u0645\u0627\u0646\u062f\u0627!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@VenomX.on_message(filters.command("repo") & ~filters.bot)
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@VenomX.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
