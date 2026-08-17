from Venom.database import users_col


async def is_served_user(user_id: int) -> bool:
    try:
        user = await users_col.find_one({"user_id": user_id})
        return user is not None
    except Exception:
        return False


async def get_served_users() -> list:
    try:
        users = await users_col.find({"user_id": {"$gt": 0}}).to_list(
            length=100_000
        )
        return users or []
    except Exception:
        return []


async def add_served_user(user_id: int):
    try:
        if await is_served_user(user_id):
            return
        await users_col.insert_one({"user_id": user_id})
    except Exception:
        pass
