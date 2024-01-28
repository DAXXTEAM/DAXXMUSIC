from pyrogram import Client, filters
from DAXXMUSIC import app
from pyrogram.types import Message




@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()
