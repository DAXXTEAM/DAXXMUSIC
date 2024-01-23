from DAXXMUSIC import app

from pyrogram import filters
from pyrogram.errors import (
    RPCError, ChatAdminRequired
)
from pyrogram.types import ChatMemberUpdated


@app.on_chat_member_updated(filters.group, group=10)
async def member_has_joined(client: app, member: ChatMemberUpdated):

    if (
        member.new_chat_member
        and member.new_chat_member.status not in {
            "banned", "left", "restricted"
        }
        and not member.old_chat_member
    ):
        pass
    else:
        return

    user = (
        member.new_chat_member.user
        if member.new_chat_member
        else member.from_user
    )
    try:
        if user.is_app:
            return
    except ChatAdminRequired:
        return
    try:
        await client.send_message(
            chat_id=member.chat.id,
            text=f"**Welcome {user.mention}**",
        )
    except RPCError as e:
        print(e)
        return



@app.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: app, member: ChatMemberUpdated):

    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {
            "banned", "restricted"
        }
        and member.old_chat_member
    ):
        pass
    else:
        return
    user = (
        member.old_chat_member.user
        if member.old_chat_member
        else member.from_user
    )
    try:
        return await client.send_message(
            chat_id=member.chat.id,
            text=f"**Goodbye {user.mention}**"
        )
    except RPCError as e:
        print(e)
        return
        
