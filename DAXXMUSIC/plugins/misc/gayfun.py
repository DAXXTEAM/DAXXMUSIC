from pyrogram import Client, filters
from pyrogram.types import Message
import random
from DAXXMUSIC import app

def calculate_gay_percentage():
    # Simple random gay percentage calculation for fun
    return random.randint(1, 100)


def generate_gay_response(gay_percentage):
    # Define random texts and emojis for different gay percentage ranges
    if gay_percentage < 30:
        return "๏ ʏᴏᴜ'ʀᴇ sᴛʀᴀɪɢʜᴛ ᴀs ᴀɴ ᴀʀʀᴏᴡ. 🏳️‍🌈"
    elif 30 <= gay_percentage < 70:
        return "๏ ʏᴏᴜ ᴍɪɢʜᴛ ʜᴀᴠᴇ ᴀ ʙɪᴛ ᴏғ ᴀ ʀᴀɪɴʙᴏᴡ ɪɴ ʏᴏᴜ. 🌈"
    else:
        return "๏ ʏᴏᴜ'ʀᴇ sʜɪɴɪɴɢ ᴡɪᴛʜ ʀᴀɪɴʙᴏᴡ ᴄᴏʟᴏʀs! 🌟🏳️‍🌈"

@app.on_message(filters.command("gay") & filters.regex(r'^/gay$'))
def gay_calculator_command(client, message: Message):
    # Calculate gay percentage
    gay_percentage = calculate_gay_percentage()

    # Generate gay response
    gay_response = generate_gay_response(gay_percentage)

    # Send the gay response as a message
    message.reply_text(f"๏ ɢᴀʏ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ ➛ {gay_percentage}%\n{gay_response}")
