import asyncio
from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from DAXXMUSIC import app
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import OWNER_ID
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.utils.daxx_ban import admin_filter
 

@app.on_message(filters.command("ban") & admin_filter)
async def ban(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id     
    user_id = message.from_user.id
    msg = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘ!")
    elif reply:
        try:
            user = reply.from_user
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.ban_member(user.id)
                await msg.edit_text(f"<code>❕</code><b>ʙᴀɴ ᴇᴠᴇɴᴛ</b>\n <b>•  ʙᴀɴɴᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
                
            else:
                await msg.edit_text("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ ᴜsᴇʀs.")
        except AttributeError:
            await msg.edit_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ʙᴀɴ ᴜsᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀs.")
    elif len(message.command) > 1:
        try:
            user = await app.get_user(message.command[1])
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.ban_member(user.id)
                await msg.edit_text(f"<code>❕</code><b>ʙᴀɴ ᴇᴠᴇɴᴛ</b>\n <b>•  ʙᴀɴɴᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)      
            else:
                await msg.edit_text("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ ᴜsᴇʀs.")
        except AttributeError:
            await msg.edit_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ʙᴀɴ ᴜsᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀs.")
        except Exception as e:
            await msg.edit_text(f"ᴇʀʀᴏʀ: {e}")
    else:
        await msg.edit_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢs ᴏʀ ɢɪᴠᴇ ᴀ ᴜsᴇʀ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ʙᴀɴ.")
