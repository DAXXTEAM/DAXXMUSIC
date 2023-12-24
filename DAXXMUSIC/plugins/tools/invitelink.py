from DAXXMUSIC import app
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant
from pyrogram.types import Message

@app.on_message(filters.command("invitelink", prefixes="/"))
async def link_command_handler(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply("Invalid usage. Correct format: /invitelink group_id")
        return
    group_id = message.command[1]

    try:
        chat = await client.get_chat(int(group_id))
        try:
            invite_link = await client.export_chat_invite_link(chat.id)
        except FloodWait as e:
            await message.reply(f"FloodWait: {e.x} seconds. Retrying in {e.x} seconds.")
            return
        file_content = (
            f"Group ID: {chat.id}\n"
            f"Group Title: {chat.title}\n"
            f"Members Count: {chat.members_count}\n"
            f"Invite Link: {invite_link}"
        )
        file_name = f"group_info_{chat.id}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(file_content)
        await client.send_document(
            chat_id=message.chat.id,
            document=file_name,
            caption=f"Here is the information for the group {chat.title}"
        )

    except Exception as e:
        await message.reply(f"Error: {str(e)}")

    finally:
        import os
        os.remove(file_name)
