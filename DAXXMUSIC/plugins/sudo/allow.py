from DAXXMUSIC import app 
from DAXXMUSIC.misc import SUDOERS
from pyrogram import filters, Client
from pyrogram.types import Message
from DAXXMUSIC.utils.chats import (get_served_chats, is_served_chat, add_served_chat, get_served_chats, remove_served_chat)  


@app.on_message(filters.command(["allow"]) & SUDOERS)
async def blacklist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "Usage:\n/allow [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if not await is_served_chat(chat_id):
        await add_served_chat(chat_id)
        await message.reply_text("✅ chat added to allowed group list")
    else:
        await message.reply_text("✅ already added to allowed list")
    
@app.on_message(filters.command(["deny"]) & SUDOERS)
async def whitelist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "usage:\n/deny [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if not await is_served_chat(chat_id):
        await message.reply_text("❌ chat not allowed.")
        return
    try:
        await remove_served_chat(chat_id)
        await message.reply_text("❌ chat has denied.")
        return
    except Exception as e:
      await message.reply_text(f"error: {e}")
