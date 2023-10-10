from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOGGER_ID as LOG_GROUP_ID
from .. import app
from DAXXMUSIC import app

async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(_, message: Message):
    if (await app.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        new = f"**✫** <b><u>#𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ</u></b> **✫**\n\n**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}\n\n**𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ :** {username}\n\n**𝐂ʜᴀᴛ 𝐈ᴅ :** {chat_id}\n\n**𝐀ᴅᴅᴇᴅ 𝐁ʏ :** {added_by}\n\n**𝐁ᴏᴛ : @{app.username}** "
        await new_message(LOG_GROUP_ID, new)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"**✫** <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> **✫**\n\n**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}\n\n**𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ :** {username}\n\n**𝐂ʜᴀᴛ 𝐈ᴅ :** {chat_id}\n\n**𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ :** {remove_by}\n\n**𝐁ᴏᴛ : @{app.username}**"
        await new_message(LOG_GROUP_ID, left)
