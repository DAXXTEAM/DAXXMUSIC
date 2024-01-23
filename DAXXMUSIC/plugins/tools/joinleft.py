from DAXXMUSIC import app

from pyrogram import filters
from pyrogram.errors import (
    RPCError, ChatAdminRequired
)
from pyrogram.types import ChatMemberUpdated

# -------------


@app.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: app, member: ChatMemberUpdated):

    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {
            "banned", "left", "restricted"
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
        
