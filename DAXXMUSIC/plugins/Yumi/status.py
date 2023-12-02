from pyrogram import Client, filters
from DAXXMUSIC import app


# Command handler to get group status
@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = f"Group ID: {chat.id}\n" \
                  f"Title: {chat.title}\n" \
                  f"Type: {chat.type}\n"
                  
    if chat.username:  # Not all groups have a username
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)


#########

""" ***                                                                       
────────────────────────────────────────────────────────────────────────
─████████████────██████████████──████████──████████──████████──████████─
─██░░░░░░░░████──██░░░░░░░░░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─██░░████░░░░██──██░░██████░░██──████░░██──██░░████──████░░██──██░░████─
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░░░░░░░░░██──────██░░░░░░██──────────██░░░░░░██─────
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░████░░░░██──██░░██──██░░██──████░░██──██░░████──████░░██──██░░████─
─██░░░░░░░░████──██░░██──██░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─████████████────██████──██████──████████──████████──████████──████████─
────────────────────────────────────────────────────────────────────────**"""




####

@app.on_message(filters.command("groupinfo") & filters.group)
def group_info_command(client, message):
    try:
        # Group Information
        group_name = message.chat.title
        group_id = message.chat.id
        total_members = client.get_chat_members_count(chat_id=group_id)

        # Get Chat Information for Description and Username
        chat_info = client.get_chat(chat_id=group_id)

        group_description = chat_info.description if chat_info.description else "No description available"
        group_username = chat_info.username if chat_info.username else "No username set"

        response_text = (
            f"Gʀᴏᴜᴘ Nᴀᴍᴇ: {group_name}\n\n"
            f"Gʀᴏᴜᴘ ID: {group_id}\n\n\"
            f"Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs: {total_members}\n\n\"
            f"Dᴇsᴄʀɪᴘᴛɪᴏɴ: {group_description}\n\n"
            f"Usᴇʀɴᴀᴍᴇ: @{group_username}"
        )

        message.reply_text(response_text)

    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")
