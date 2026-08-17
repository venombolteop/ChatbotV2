from pyrogram import filters, Client
from pyrogram.types import Message

from Venom import OWNER, VenomX
from Venom.database.chats import get_served_chats
from Venom.database.users import get_served_users


@VenomX.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""\u062a\u0648\u062a\u0627\u0644 \u0627\u0637\u0644\u0627\u0639\u0627\u062a {(await cli.get_me()).mention} :

\u2773 **\u0686\u0627\u062a\u0647\u0627 :** {chats}
\u2773 **\u06a9\u0627\u0631\u0628\u0631\u0627\u0646 :** {users}"""
    )
