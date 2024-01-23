from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.left_chat_member)
async def member_has_left(_, m: Message):
    left_gif = "https://telegra.ph/file/d28047520fad932521368.mp4"
    await m.reply_animation(
        animation=left_gif,
        caption=f"Sᴀᴅ Tᴏ Sᴇᴇ Yᴏᴜ Lᴇᴀᴠɪɴɢ {m.left_chat_member.mention}\nTᴀᴋᴇ Cᴀʀᴇ!"
    )
    
