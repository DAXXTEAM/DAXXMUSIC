from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from DAXXMUSIC import app


def get_pypi_info(package_name):
    try:
        
        api_url = f"https://pypi.org/pypi/{package_name}/json"
        
        # Sending a request to the PyPI API
        response = requests.get(api_url)
        
        # Extracting information from the API response
        pypi_info = response.json()
        
        return pypi_info
    
    except Exception as e:
        print(f"Error fetching PyPI information: {e}")
        return None

@app.on_message(filters.command("pypi", prefixes="/"))
def pypi_info_command(client, message):
    try:
       
        package_name = message.command[1]
        
        # Getting information from PyPI
        pypi_info = get_pypi_info(package_name)
        
        if pypi_info:
            # Creating a message with PyPI information
            info_message = f"ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ➪ {pypi_info['info']['name']}\n\n" \
                           f"Lᴀᴛᴇsᴛ ᴠɪʀsɪᴏɴ➪ {pypi_info['info']['version']}\n\n" \
                           f"Dᴇsᴄʀɪᴘᴛɪᴏɴ➪ {pypi_info['info']['summary']}\n\n" \
                           f"ᴘʀᴏJᴇᴄᴛ ᴜʀʟ➪ {pypi_info['info']['project_urls']['Homepage']}"
            
            # Sending the PyPI information back to the user
            client.send_message(message.chat.id, info_message)
        
        else:
            # Handling the case where information retrieval failed
            client.send_message(message.chat.id, "Failed to fetch information from PyPI.")
    
    except IndexError:

        client.send_message(message.chat.id, "Please provide a package name after the /pypi command.")
