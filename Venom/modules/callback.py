from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from Venom import VenomX
from Venom.database import vick_col
from Venom.modules.helpers import (
    ABOUT_BTN,
    ABOUT_READ,
    ADMIN_READ,
    BACK,
    CHATBOT_BACK,
    CHATBOT_READ,
    DEV_OP,
    HELP_BTN,
    HELP_READ,
    MUSIC_BACK_BTN,
    SOURCE_READ,
    START,
    TOOLS_DATA_READ,
)


@VenomX.on_callback_query()
async def cb_handler(_, query: CallbackQuery):
    try:
        if query.data == "HELP":
            await query.message.edit_text(
                text=HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BTN),
                disable_web_page_preview=True,
            )

        elif query.data == "CLOSE":
            await query.message.delete()
            await query.answer("\u06a9\u0644\u0648\u0633 \u0645\u0646\u0648!", show_alert=True)

        elif query.data == "BACK":
            await query.message.edit(
                text=START,
                reply_markup=InlineKeyboardMarkup(DEV_OP),
            )

        elif query.data == "SOURCE":
            await query.message.edit(
                text=SOURCE_READ,
                reply_markup=InlineKeyboardMarkup(BACK),
                disable_web_page_preview=True,
            )

        elif query.data == "ABOUT":
            await query.message.edit(
                text=ABOUT_READ,
                reply_markup=InlineKeyboardMarkup(ABOUT_BTN),
                disable_web_page_preview=True,
            )

        elif query.data == "ADMINS":
            await query.message.edit(
                text=ADMIN_READ,
                reply_markup=InlineKeyboardMarkup(MUSIC_BACK_BTN),
            )

        elif query.data == "TOOLS_DATA":
            await query.message.edit(
                text=TOOLS_DATA_READ,
                reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
            )

        elif query.data == "BACK_HELP":
            await query.message.edit(
                text=HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BTN),
            )

        elif query.data == "CHATBOT_CMD":
            await query.message.edit(
                text=CHATBOT_READ,
                reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
            )

        elif query.data == "CHATBOT_BACK":
            await query.message.edit(
                text=HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BTN),
            )

        elif query.data.startswith("runtime"):
            runtime = query.data.split(None, 1)[1]
            await query.answer(runtime, show_alert=True)

        elif query.data.startswith("forceclose"):
            callback_request = query.data.split(None, 1)[1]
            _, user_id = callback_request.split("|")
            if query.from_user.id != int(user_id):
                try:
                    return await query.answer(
                        "\u00bb \u0627\u06cc\u062a\u0651\u0644 \u0628\u0647\u062a\u0631 \u0627\u0632 \u0627\u06cc\u0646 \u0645\u062d\u06f1\u062f\u0648\u062f \u0628\u0627\u0634\u06cc.",
                        show_alert=True,
                    )
                except Exception:
                    return
            await query.message.delete()
            try:
                await query.answer()
            except Exception:
                return

        elif query.data == "addchat":
            user_id = query.from_user.id
            user_status = (
                await query.message.chat.get_member(user_id)
            ).status
            if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
                return await query.answer(
                    "\u0627\u06cc\u062a \u062d\u0634 \u0627\u062f\u0645\u064a\u0646 \u0646\u0633\u062a\u06cc\u062f, "
                    "\u0627\u0632 \u0627\u06cc\u0646 \u062c\u0631\u064a\u0645\u0647 \u062e\u0648\u062f \u0631\u0648 \u0627\u0645\u062a\u062d\u0627\u0646!",
                    show_alert=True,
                )
            is_vick = await vick_col.find_one(
                {"chat_id": query.message.chat.id}
            )
            if not is_vick:
                await query.edit_message_text(
                    "**\u0686\u0627\u062a-\u0628\u0648\u062a \u0642\u0628\u0644\u0627 \u0641\u0639\u0627\u0644 \u0634\u062f\u0647.**"
                )
            if is_vick:
                await vick_col.delete_one(
                    {"chat_id": query.message.chat.id}
                )
                await query.edit_message_text(
                    f"**\u0686\u0627\u062a-\u0628\u0648\u062a \u0641\u0639\u0627\u0644 \u0634\u062f\u0647 \u062a\u0648\u0633\u0637** "
                    f"{query.from_user.mention}."
                )

        elif query.data == "rmchat":
            user_id = query.from_user.id
            user_status = (
                await query.message.chat.get_member(user_id)
            ).status
            if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
                await query.answer(
                    "\u0627\u06cc\u062a \u062d\u0634 \u0627\u062f\u0645\u064a\u0646 \u0646\u0633\u062a\u06cc\u062f, "
                    "\u0627\u0632 \u0627\u06cc\u0646 \u062c\u0631\u064a\u0645\u0647 \u062e\u0648\u062f \u0631\u0648 \u0627\u0645\u062a\u062d\u0627\u0646!",
                    show_alert=True,
                )
                return
            is_vick = await vick_col.find_one(
                {"chat_id": query.message.chat.id}
            )
            if not is_vick:
                await vick_col.insert_one(
                    {"chat_id": query.message.chat.id}
                )
                await query.edit_message_text(
                    f"**\u0686\u0627\u062a-\u0628\u0648\u062a \u063a\u06cc\u0631\u0641\u0639\u0627\u0644 \u0634\u062f\u0647 \u062a\u0648\u0633\u0637** "
                    f"{query.from_user.mention}."
                )
            if is_vick:
                await query.edit_message_text(
                    "**\u0686\u0627\u062a-\u0628\u0648\u062a \u0642\u0628\u0644\u0627 \u063a\u06cc\u0631\u0641\u0639\u0627\u0644 \u0634\u062f\u0647.**"
                )

    except Exception:
        pass
