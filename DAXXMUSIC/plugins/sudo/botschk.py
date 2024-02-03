from DAXXMUSIC.misc import db
from DAXXMUSIC.utils.database import get_assistant, get_authuser_names, get_cmode

import asyncio
import config
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

from datetime import datetime
from pyrogram.enums import ChatType
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.logging import LOGGER
from config import *
from DAXXMUSIC import app, userbot
from DAXXMUSIC.core.userbot import Client
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.core import *




BOT_LIST = ["NexikoBot", "GitWizardBot", "urXdestinyBot"]





@app.on_message(filters.command("botschk") & SUDOERS)
async def bots_chk(app, message):
    msg = await message.reply_photo(photo="https://telegra.ph/file/48578068b7574bb25a529.jpg", caption="**ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ...**")
    response = "**ʙᴏᴛs sᴛᴀᴛᴜs ᴅᴇᴀᴅ ᴏʀ ᴀʟɪᴠᴇ ᴄʜᴇᴄᴋᴇʀ**\n\n"
    for bot_username in BOT_LIST:
        try:
            bot = await userbot.get_users(bot_username)
            bot_id = bot.id
            await asyncio.sleep(0.5)
            bot_info = await userbot.send_message(bot_id, "/start")
            await asyncio.sleep(3)
            async for bot_message in userbot.get_chat_history(bot_id, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**\n\n"
                else:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴇʀʀᴏʀ ❌**\n"
    
    await msg.edit_text(response)
