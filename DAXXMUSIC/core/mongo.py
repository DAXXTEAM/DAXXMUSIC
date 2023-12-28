from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐧𝐠 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐌𝐨𝐧𝐠𝐨 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐌𝐨𝐧𝐠𝐨 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞.")
except:
    LOGGER(__name__).error("𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐜𝐨𝐧𝐧𝐞𝐜𝐭 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐌𝐨𝐧𝐠𝐨 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞.")
    exit()
