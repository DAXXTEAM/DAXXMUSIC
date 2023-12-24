/eval from DAXXMUSIC import app
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant

@app.on_message(filters.command("invitelink"))
def get_invite_link(client, message):
    if message.text:
        try:
            if message.chat.type == 'private':
                group_id = int(message.text.split(" ")[1])
            else:
                group_id = message.chat.id
            
            try:
                invite_link = app.export_chat_invite_link(group_id)
                message.reply_text(f"Here is the invite link for the group {group_id}: {invite_link}")
            except (ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant) as e:
                error_message = str(e)
                if "not enough rights" in error_message.lower():
                    message.reply_text("I don't have the necessary permissions to invite users to this group.")
                elif "chat not found" in error_message.lower():
                    message.reply_text("The specified group does not exist.")
                else:
                    message.reply_text(f"Error: {error_message}")
        except (IndexError, ValueError):
            message.reply_text("Invalid command. Please use /invitelink <group_id>")
