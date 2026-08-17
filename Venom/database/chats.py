from Venom.database import chats_col


async def get_served_chats() -> list:
    try:
        chats = await chats_col.find({"chat_id": {"$lt": 0}}).to_list(
            length=100_000
        )
        return chats or []
    except Exception:
        return []


async def is_served_chat(chat_id: int) -> bool:
    try:
        chat = await chats_col.find_one({"chat_id": chat_id})
        return chat is not None
    except Exception:
        return False


async def add_served_chat(chat_id: int):
    try:
        if await is_served_chat(chat_id):
            return
        await chats_col.insert_one({"chat_id": chat_id})
    except Exception:
        pass


async def remove_served_chat(chat_id: int):
    try:
        if not await is_served_chat(chat_id):
            return
        await chats_col.delete_one({"chat_id": chat_id})
    except Exception:
        pass
