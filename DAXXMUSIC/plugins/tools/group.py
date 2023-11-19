from pyrogram import Client, filters
from DAXXMUSIC import app

@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ")
