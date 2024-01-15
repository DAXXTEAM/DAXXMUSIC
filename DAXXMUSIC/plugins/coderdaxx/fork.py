from pyrogram import Client, filters
import requests
from urllib.parse import urlparse
from DAXXMUSIC import app 
from config import OWNER_ID

github_token = "YOUR GIT TOKEN"


@app.on_message(filters.command("fork") & filters.user(OWNER_ID))
def fork_command(client, message):
    
    chat_id = message.chat.id

    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        message.reply_text("Iɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ. Usᴇ /frok [ʀᴇᴘᴏsɪᴛᴏʀʏ_ᴜʀʟ]")
        return

    repo_url = command_parts[1]
    repo_info = urlparse(repo_url)

    if not repo_info.netloc or not repo_info.path:
        message.reply_text("Iɴᴠᴀʟɪᴅ ʀᴇᴘᴏsɪᴛᴏʀʏ URL. Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ URL")
        return
        
    fork_url = f"https://api.github.com/repos{repo_info.path}/forks"
    headers = {"Authorization": f"token {github_token}"}

    response = requests.post(fork_url, headers=headers)

    if response.status_code == 202:
        message.reply_text("Yᴏᴜʀ Rᴇᴘᴏ sᴜᴄᴄᴇssғᴜʟ ᴜᴘʟᴏᴀᴅ ᴄʜᴇᴄᴋ ʏᴏᴜʀ Gɪᴛʜᴜʙ!")
    else:
        message.reply_text("Fᴀɪʟᴇᴅ ᴛᴏ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ. Pʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄʀᴇᴅᴇɴᴛɪᴀʟs ᴏʀ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ URL.")
