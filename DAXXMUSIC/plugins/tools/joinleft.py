from DAXXMUSIC import app
from pyrogram import filters
from pyrogram.errors import RPCError, ChatAdminRequired
from pyrogram.types import ChatMemberUpdated

# -------------

@app.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: app, member: ChatMemberUpdated):
    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {"banned", "left", "restricted"}
        and member.old_chat_member
    ):
        pass
    else:
        return

    user = (
        member.old_chat_member.user if member.old_chat_member else member.from_user
    )
    
    try:
        caption = f"Sᴀᴅ Tᴏ Sᴇᴇ Yᴏᴜ Lᴇᴀᴠɪɴɢ {user.mention}\nTᴀᴋᴇ Cᴀʀᴇ!"
        left_gif = "https://graph.org/file/db6dec1e9bc0b14e9e842.mp4"
        
        await client.send_animation(
            chat_id=member.chat.id,
            animation=left_gif,
            caption=caption
        )
    except RPCError as e:
        print(e)
        return
        
