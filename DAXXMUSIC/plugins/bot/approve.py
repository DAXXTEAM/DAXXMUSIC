from DAXXMUSIC import app
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from typing import Union, Optional



# --------------------------------------------------------------------------------- #


get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #


async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )


    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path
   

# --------------------------------------------------------------------------------- #

bg_path = "DAXXMUSIC/assets/userinfo.png"
font_path = "DAXXMUSIC/assets/hiroko.ttf"

# --------------------------------------------------------------------------------- #

# Extract environment variables or provide default values
chat_id_env = environ.get("CHAT_ID")
CHAT_ID = [int(app) for app in chat_id_env.split(",")] if chat_id_env else []

TEXT = environ.get("APPROVED_WELCOME_TEXT", "**❅─────✧❅✦❅✧─────❅**\n**🥀ʜᴇʏ {mention}**\n\n**🏓ᴡᴇʟᴄᴏᴍᴇ ɪɴ ɴᴇᴡ ɢʀᴏᴜᴘ✨**\n\n**➻** {title}\n\n**💞ɴᴏᴡ ᴍᴀᴋᴇ ɴᴇᴡ ғʀɪᴇɴᴅs ᴀɴᴅ sᴛᴀʏ ᴀʟᴡᴀʏs ᴏɴʟɪɴᴇ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ🥳**\n**❅─────✧❅✦❅✧─────❅**")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# List of random photo links
random_photo_links = [
    "https://telegra.ph/file/ca950c0b8316b968957fa.jpg",
    "https://telegra.ph/file/ca950c0b8316b968957fa.jpg",
    "https://telegra.ph/file/ca950c0b8316b968957fa.jpg",
    # Add more links as needed
]

# Define an event handler for chat join requests
@app.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: app, message: ChatJoinRequest):
    chat = message.chat  # Chat
    user = message.from_user  # User
    photo = await app.download_media(user.photo.big_file_id)

    # Fix the indentation here
    welcome_photo = await get_userinfo_img(
        bg_path=bg_path,
        font_path=font_path,
        user_id=user.id,
        profile_path=photo,
    )

    print(f"{user.first_name} Joined 🤝")  # Logs

  
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)

    if APPROVED == "on":
        await client.send_photo(
            chat_id=chat.id,
            photo=welcome_photo,
            caption=TEXT.format(mention=user.mention, title=chat.title),
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ๏ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ๏ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
            ]
        ),
                    )

        
