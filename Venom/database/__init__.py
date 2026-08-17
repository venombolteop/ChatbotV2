import logging

from pymongo import AsyncMongoClient

import config

LOGGER = logging.getLogger(__name__)

_client = AsyncMongoClient(config.MONGO_URL)

_anonymous = _client["Anonymous"]
_word = _client["Word"]
_vickdb = _client["VickDb"]

chats_col = _anonymous["chatsdb"]
users_col = _anonymous["users"]
word_col = _word["WordDb"]
vick_col = _vickdb["Vick"]

vick = vick_col


async def init_indexes():
    try:
        await chats_col.create_index("chat_id", unique=True)
        await users_col.create_index("user_id", unique=True)
        await word_col.create_index("word")
        await word_col.create_index([("word", 1), ("text", 1)])
        await vick_col.create_index("chat_id", unique=True)
        LOGGER.info("Database indexes created successfully.")
    except Exception as e:
        LOGGER.error(f"Failed to create indexes: {e}")


async def close_db():
    try:
        _client.close()
        LOGGER.info("Database connection closed.")
    except Exception as e:
        LOGGER.error(f"Error closing database: {e}")


from .chats import *  # noqa: E402, F401, F403
from .users import *  # noqa: E402, F401, F403
