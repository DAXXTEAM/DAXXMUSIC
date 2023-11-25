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




@app.on_message(filters.command(["unbanall"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
async def unban(event):
   if event.sender_id in SUDOERS:
     if not event.is_group:
         Reply = f"Noob !! Use This Cmd in Group."
         await event.reply(Reply)
     else:
         msg = await event.reply("Searching Participant Lists.")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sleeping for {ex.seconds} seconds")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} unbanned".format(event.chat_id, p))