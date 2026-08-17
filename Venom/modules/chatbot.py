import random
import re

from pyrogram import filters
from pyrogram.enums import ChatAction, ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, Message

from Venom import LOGGER, VenomX
from Venom.database import vick_col, word_col
from Venom.modules.helpers import CHATBOT_ON

_SPAM_RE = re.compile(
    r"https?://|"
    r"t\.me/|"
    r"www\.|"
    r"tg://|"
    r"@\w{3,}",
    re.IGNORECASE,
)


def _is_clean(text: str) -> bool:
    return _SPAM_RE.search(text) is None


async def _find_response(input_key: str):
    if isinstance(input_key, str) and not _is_clean(input_key):
        return None, "text"
    try:
        results = await word_col.find({"word": input_key}).to_list(length=100)
        if not results:
            return None, "text"
        chosen = random.choice(results)
        return chosen["text"], chosen.get("check", "text")
    except Exception as e:
        LOGGER.error(f"Error finding response: {e}")
        return None, "text"


async def _learn(stored_word: str, stored_text: str, check_type: str):
    if not _is_clean(stored_word) or not _is_clean(stored_text):
        return
    try:
        existing = await word_col.find_one(
            {"word": stored_word, "text": stored_text}
        )
        if not existing:
            await word_col.insert_one(
                {
                    "word": stored_word,
                    "text": stored_text,
                    "check": check_type,
                }
            )
    except Exception as e:
        LOGGER.error(f"Error learning: {e}")


async def _is_chatbot_disabled(chat_id: int) -> bool:
    try:
        return await vick_col.find_one({"chat_id": chat_id}) is not None
    except Exception:
        return False


async def _reply_with_response(message: Message, response: str, check_type: str):
    try:
        if check_type == "sticker":
            await message.reply_sticker(response)
        else:
            await message.reply_text(response)
    except Exception as e:
        LOGGER.error(f"Error replying: {e}")


@VenomX.on_message(filters.command("chatbot") & filters.group & ~filters.bot)
async def chatbot_command(client, message: Message):
    try:
        user = await client.get_chat_member(
            message.chat.id, message.from_user.id
        )
        if user.status not in (
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR,
        ):
            return await message.reply_text(
                "You need admin rights to toggle chatbot."
            )
    except Exception:
        return await message.reply_text(
            "Failed to verify your admin status."
        )
    await message.reply_text(
        f"Chat: {message.chat.title}\n"
        "**Choose an option to enable/disable chatbot.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )


@VenomX.on_message(
    (filters.text | filters.sticker) & filters.group & ~filters.bot,
    group=4,
)
async def group_chatbot(client, message: Message):
    if message.text and message.text.startswith(("/", "!", "?", "@", "#")):
        return

    try:
        if await _is_chatbot_disabled(message.chat.id):
            return
    except Exception:
        return

    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    if message.sticker:
        input_key = message.sticker.file_unique_id
    elif message.text:
        input_key = message.text
    else:
        return

    if message.reply_to_message:
        if message.reply_to_message.from_user.id == client.id:
            response, check_type = await _find_response(input_key)
            if response:
                await _reply_with_response(message, response, check_type)
            return

        if message.reply_to_message.from_user.id != client.id:
            original = message.reply_to_message
            if original.sticker:
                stored_word = original.sticker.file_unique_id
            elif original.text:
                stored_word = original.text
            else:
                return
            if message.sticker:
                await _learn(stored_word, message.sticker.file_id, "sticker")
            elif message.text:
                await _learn(stored_word, message.text, "text")
            return

    response, check_type = await _find_response(input_key)
    if response:
        await _reply_with_response(message, response, check_type)


@VenomX.on_message(
    (filters.text | filters.sticker) & filters.private & ~filters.bot,
    group=4,
)
async def private_chatbot(client, message: Message):
    if message.text and message.text.startswith(("/", "!", "?", "@", "#")):
        return

    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    if message.sticker:
        input_key = message.sticker.file_unique_id
    elif message.text:
        input_key = message.text
    else:
        return

    if message.reply_to_message:
        if message.reply_to_message.from_user.id == client.id:
            response, check_type = await _find_response(input_key)
            if response:
                await _reply_with_response(message, response, check_type)
            return

        if message.reply_to_message.from_user.id != client.id:
            original = message.reply_to_message
            if original.sticker:
                stored_word = original.sticker.file_unique_id
            elif original.text:
                stored_word = original.text
            else:
                return
            if message.sticker:
                await _learn(stored_word, message.sticker.file_id, "sticker")
            elif message.text:
                await _learn(stored_word, message.text, "text")
            return

    response, check_type = await _find_response(input_key)
    if response:
        await _reply_with_response(message, response, check_type)
