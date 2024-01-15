from pyrogram import Client, filters
import requests
from DAXXMUSIC import app as bot
from config import OWNER_ID

"""**
Copyright (c) 2024, DAXXTEAM
All rights reserved.

# Your actual Python code starts here
def my_function():
    # Function implementation
    pass
**"""
 

@bot.on_message(filters.command("delrepo"))
def delete_repo(client, message):
    try:
        # Ensure that only the owner can use this command
        if message.from_user.id != OWNER_ID:
            message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")
            return

        # Extracting URL from the command
        url = message.text.split(" ", 1)[1].strip()

        # Assuming the URL is in the format 'https://github.com/Daxxteam/repo'
        parts = url.split("/")
        username, repo_name = parts[-2], parts[-1]

        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
        github_token = "YOU'RE GIT TOKEN"
        headers = {"Authorization": f"token {github_token}"}

        # Delete the repository using GitHub API
        response = requests.delete(f"https://api.github.com/repos/{username}/{repo_name}", headers=headers)

        if response.status_code == 204:
            message.reply_text(f"Rᴇᴘᴏsɪᴛᴏʀʏ {username}/{repo_name}sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ.")
        else:
            message.reply_text(f"Fᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ. Sᴛᴀᴛᴜs ᴄᴏᴅᴇ {response.status_code}")

    except IndexError:
        message.reply_text("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ URL ᴀғᴛᴇʀ ᴛʜᴇ /ᴅᴇʟʀᴇᴘᴏ ᴄᴏᴍᴍᴀɴᴅ")
    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")
  
