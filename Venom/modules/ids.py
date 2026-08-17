from pyrogram import filters
from pyrogram.enums import ParseMode

from Venom import VenomX


@VenomX.on_message(filters.command("id") & ~filters.bot)
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[\u0645\u0633\u062c \u0627\u06cc\u06f1\u062f:]({message.link})** `{message_id}`\n"
    text += f"**[\u064a\u0627\u06f1\u062f \u0627\u06cc\u06f1\u062f:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[\u06a9\u0627\u0631\u0628\u0631 \u0627\u06cc\u06f1\u062f:](tg://user?id={user_id})** `{user_id}`\n"
        except Exception:
            return await message.reply_text(
                "\u0627\u06cc\u0646 \u06a9\u0627\u0631\u0628\u0631 \u0648\u062c\u0648\u06f1\u062f \u0646\u062f\u0627\u0631\u062f.",
                quote=True,
            )

    text += f"**[\u0686\u0627\u062a \u0627\u06cc\u06f1\u062f:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[\u0645\u0633\u062c \u067e\u0627\u0633\u062e \u0627\u06cc\u06f1\u062f:]({reply.link})** `{reply.id}`\n"
        text += f"**[\u06a9\u0627\u0631\u0628\u0631 \u067e\u0627\u0633\u062e:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += (
            f"\u0627\u0632 \u0633\u0648\u0627\u0646\u06f1\u062f\u0647 \u0634\u062f\u0647, "
            f"{reply.forward_from_chat.title}, \u0627\u06cc\u06f1\u062f \u0627\u0634 "
            f"`{reply.forward_from_chat.id}` \u0627\u0633\u062a\n\n"
        )

    if reply and reply.sender_chat:
        text += (
            f"\u0627\u06cc\u06f1\u062f \u062a\u0646\u0638\u0631 \u0628\u0627\u0632\u06af\u0634\u062a\u0647 "
            f"\u0634\u062f\u0647/\u06a9\u0646\u0627\u0644, {reply.sender_chat.id}\u0627\u0633\u062a"
        )

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )
