import asyncio
from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from DAXXMUSIC import app
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import OWNER_ID
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.utils.daxx_ban import admin_filter
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)



button = InlineKeyboardMarkup(
        [[
         InlineKeyboardButton(" ᴄʟᴏsᴇ ",callback_data="close_data")
        ]])



@app.on_message(filters.command("ban", COMMAND_HANDLER) & admin_filter)
async def ban(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id     
    user_id = message.from_user.id
    msg = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘ!**")
    elif reply:
        try:
            user = reply.from_user
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.ban_member(user.id)
                await msg.edit_text(f"<code>❕</code><b>ʙᴀɴ ᴇᴠᴇɴᴛ</b>\n <b>•  ʙᴀɴɴᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
                
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ ᴜsᴇʀs.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ʙᴀɴ ᴜsᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀs.**")
    elif len(message.command) > 1:
        try:
            user = await app.get_user(message.command[1])
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.ban_member(user.id)
                await msg.edit_text(f"<code>❕</code><b>ʙᴀɴ ᴇᴠᴇɴᴛ</b>\n <b>•  ʙᴀɴɴᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)      
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ʙᴀɴ ᴜsᴇʀs.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ʙᴀɴ ᴜsᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀs.**")
        except Exception as e:
            await msg.edit_text(f"**ᴇʀʀᴏʀ:** {e}")
    else:
        await msg.edit_text("**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢs ᴏʀ ɢɪᴠᴇ ᴀ ᴜsᴇʀ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ʙᴀɴ.**")



@app.on_message(filters.command("unban", COMMAND_HANDLER) & admin_filter)
async def unban(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs!**")
    elif reply:
        try:
            user = reply.from_user
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.unban_member(user.id)
                await msg.edit_text(f"<code>❕</code><b>ᴜɴʙᴀɴ ᴇᴠᴇɴᴛ</b>\n <b>•  ʙᴀɴɴᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
                                       
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀs.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜɴʙᴀɴ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs.**")
    elif len(message.command) > 1:
        try:
            user = await app.get_user(message.command[1])
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.unban_member(user.id)
                await msg.edit_text(f"<code>❕</code><b>ᴜɴʙᴀɴ ᴇᴠᴇɴᴛ</b>\n <b>•  ʙᴀɴɴᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴʙᴀɴ.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜɴʙᴀɴ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs.**")
        except Exception as e:
            await msg.edit_text(f"**Error:** {e}")
    else:
        await msg.edit_text("**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴀ ᴜsᴇʀ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀ.**")



 
@app.on_message(filters.command("mute", COMMAND_HANDLER) & admin_filter)
async def mute(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs!**")
    elif reply:
        try:
            user = reply.from_user
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.restrict_member(user.id,permissions=ChatPermissions(can_send_messages=False),)
                await msg.edit_text(f"<code>❕</code><b>ᴍᴜᴛᴇ ᴇᴠᴇɴᴛ</b>\n <b>•  ᴍᴜᴛᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
                                       
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴍᴜᴛᴇ ᴜsᴇʀs.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴍᴜᴛᴇ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs.**")
    elif len(message.command) > 1:
        try:
            user = await app.get_user(message.command[1])
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.restrict_member(user.id,permissions=ChatPermissions(can_send_messages=False),)    
                await msg.edit_text(f"<code>❕</code><b>ᴍᴜᴛᴇ ᴇᴠᴇɴᴛ</b>\n <b>•  ᴍᴜᴛᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴍᴜᴛᴇ ᴜsᴇʀ.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴍᴜᴛᴇ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs.**")
        except Exception as e:
            await msg.edit_text(f"**Error:** {e}")
    else:
        await msg.edit_text("**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴀ ᴜsᴇʀ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀ.**")



@app.on_message(filters.command("unmute", COMMAND_HANDLER) & admin_filter)
async def unmute(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs!**")
    elif reply:
        try:
            user = reply.from_user
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.restrict_member(user.id,permissions=ChatPermissions(can_send_messages=True),)
                await msg.edit_text(f"<code>❕</code><b>ᴜɴᴍᴜᴛᴇ ᴇᴠᴇɴᴛ</b>\n <b>•  ᴜɴᴍᴜᴛᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
                                       
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴜsᴇʀs.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜɴᴍᴜᴛᴇ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs.**")
    elif len(message.command) > 1:
        try:
            user = await app.get_user(message.command[1])
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.restrict_member(user.id,permissions=ChatPermissions(can_send_messages=True),)    
                await msg.edit_text(f"<code>❕</code><b>ᴍᴜᴛᴇ ᴇᴠᴇɴᴛ</b>\n <b>•  ᴍᴜᴛᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴᴍᴜᴛᴇ ᴜsᴇʀ.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜɴᴍᴜᴛᴇ ᴜsᴇʀs ɪɴ ɢʀᴏᴜᴘs.**")
        except Exception as e:
            await msg.edit_text(f"**Error:** {e}")
    else:
        await msg.edit_text("**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴀ ᴜsᴇʀ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀ.**")



@app.on_message(filters.command("kick", COMMAND_HANDLER) & admin_filter)
async def kick(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id     
    user_id = message.from_user.id
    msg = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘ!**")
    elif reply:
        try:
            user = reply.from_user
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.ban_member(user.id)
                await asyncio.sleep(1)
                await message.chat.unban_member(user.id)
                await msg.edit_text(f"<code>❕</code><b>ᴋɪᴄᴋ ᴇᴠᴇɴᴛ</b>\n <b>•  ᴋɪᴄᴋᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)
                
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴋɪᴄᴋ ᴜsᴇʀs.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴋɪᴄᴋ ᴜsᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀs.**")
    elif len(message.command) > 1:
        try:
            user = await app.get_user(message.command[1])
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_restrict_members:
                await message.chat.ban_member(user.id)
                await asyncio.sleep(1)
                await message.chat.unban_member(user.id)
                
                await msg.edit_text(f"<code>❕</code><b>ᴋɪᴄᴋ ᴇᴠᴇɴᴛ</b>\n <b>•  ᴋɪᴄᴋᴇᴅ ʙʏ:</b> {message.from_user.mention}\n <b>•  ᴜsᴇʀ:</b> [{user.first_name}](tg://user?id={user.id})", reply_markup=button)      
            else:
                await msg.edit_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴋɪᴄᴋ ᴜsᴇʀs.**")
        except AttributeError:
            await msg.edit_text("**ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴋɪᴄᴋ ᴜsᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀs.**")
        except Exception as e:
            await msg.edit_text(f"**ᴇʀʀᴏʀ:** {e}")
    else:
        await msg.edit_text("**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢs ᴏʀ ɢɪᴠᴇ ᴀ ᴜsᴇʀ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴋɪᴄᴋ.**")





@app.on_message(filters.command("halfpromote") & admin_filter)
async def halfpromote(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id     
    user_id = message.from_user.id
    msg = await message.reply_text("Processing...")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("This command works on groups only!")
    elif reply:
        try:
            user = reply.from_user
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.can_promote_members:
                await message.chat.promote_member(user.id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                ))
                await msg.edit_text(f"❕Promote Event\n •  Promoted by: {message.from_user.mention}\n •  User: [{user.first_name}](tg://user?id={user.id})")
            else:
                await msg.edit_text("You don't have enough permission to promote users.")
        except AttributeError:
            await msg.edit_text("You can only promote group users.")
    elif len(message.command) > 1:
        try:
            user = await app.get_user(message.command[1])
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.can_promote_members:
                await message.chat.promote_member(user.id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                ))
                await msg.edit_text(f"❕Promote Event\n •  Promoted by: {message.from_user.mention}\n •  User: [{user.first_name}](tg://user?id={user.id})")
            else:
                await msg.edit_text("You don't have enough permission to promote users.")
        except AttributeError:
            await msg.edit_text("You can only promote group users.")
        except Exception as e:
            await msg.edit_text(f"Error: {e}")
    else:
        await msg.edit_text("You need to reply to a message or give a user ID or username to promote.")



