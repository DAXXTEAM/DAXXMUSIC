from async_pymongo import AsyncClient

from config import MONGO_DB_URI

DBNAME = "THEINDIANPOLICE92DB"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]






# MADE BY SHALINI
#TELEGRAM - @itz_SHALINI
