import re
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram.types import Message
from pyrogram import Client, filters
from DAXXMUSIC import app



# "/gn" command ka handler
@app.on_message(filters.command("oodnight", prefixes="g"))
def goodnight_command_handler(client: Client, message: Message):
    # Randomly decide whether to send a sticker or an emoji
    send_sticker = random.choice([True, False])
    
    # Send a sticker or an emoji based on the random choice
    if send_sticker:
        client.send_sticker(message.chat.id, get_random_sticker())
    else:
        client.send_message(message.chat.id, get_random_emoji())

# Function to get a random sticker
def get_random_sticker():
    stickers = [
        "CAACAgQAAx0Ce9_hCAACaEVlwn7HeZhgwyVfKHc3WUGC_447IAACLgwAAkQwKVPtub8VAR018x4E",
        "CAACAgIAAx0Ce9_hCAACaEplwn7dvj7G0-a1v3wlbN281RMX2QACUgwAAligOUoi7DhLVTsNsh4E",
        "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA",
        "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",
        "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",
    ]
    return random.choice(stickers)

# Function to get a random emoji
def get_random_emoji():
    emojis = [
        "😴",
        "😪", 
        "💤",
        
    ]
    return random.choice(emojis)
