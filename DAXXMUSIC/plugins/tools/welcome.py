from VIPMUSIC import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
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

bg_path = "VIPMUSIC/assets/userinfo.png"
font_path = "VIPMUSIC/assets/hiroko.ttf"

# --------------------------------------------------------------------------------- #

# Function to handle both new members and members who have left
async def handle_member_update(client: app, member: ChatMemberUpdated):
    chat = member.chat
    
    count = await app.get_chat_members_count(chat.id)
   
    user = member.new_chat_member.user if member.new_chat_member else member.old_chat_member.user
    try:
        # Add the photo path, caption, and button details
        photo = await app.download_media(user.photo.big_file_id)

        welcome_photo = await get_userinfo_img(
            bg_path=bg_path,
            font_path=font_path,
            user_id=user.id,
            profile_path=photo,
        )

        # Assuming you have a way to obtain the member count
        

        if member.new_chat_member:
            # Welcome message for new members
            caption = (
            f"**🌷𝐇ᴇʏ {member.new_chat_member.user.mention}**\n\n**🏘𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
            f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {chat.title}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍: @{chat.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**💖𝐔ʀ 𝐈d: {member.new_chat_member.user.id}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**✍️𝐔ʀ 𝐔.𝐍: @{member.new_chat_member.user.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            button_text = "๏ ᴠɪᴇᴡ ᴘʀᴏғɪʟᴇ ๏"
        else:
            # Farewell message for members who have left
            caption = f"**❅─────✧❅✦❅✧─────❅**\n\n**๏ ᴀ ᴍᴇᴍʙᴇʀ ʟᴇғᴛ ᴛʜᴇ ɢʀᴏᴜᴘ🥀**\n\n**➻** {member.old_chat_member.user.mention}\n\n**๏ ɢᴏᴏᴅʙʏᴇ ᴀɴᴅ ʜᴏᴘᴇ ᴛᴏ sᴇᴇ ʏᴏᴜ ᴀɢᴀɪɴ sᴏᴏɴ ɪɴ ᴛʜɪs ᴄᴜᴛᴇ ɢʀᴏᴜᴘ✨**\n\n**ㅤ•─╼⃝𖠁 ʙʏᴇ ♡︎ ʙᴀʙʏ 𖠁⃝╾─•**"
            button_text = "๏ ᴠɪᴇᴡ ʟᴇғᴛ ᴍᴇᴍʙᴇʀ ๏"

        # Generate a deep link to open the user's profile
        deep_link = f"tg://openmessage?user_id={user.id}"

        # Send the message with the photo, caption, and button
        await client.send_photo(
            chat_id=member.chat.id,
            photo=welcome_photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(button_text, url=deep_link)]
            ])
        )
    except RPCError as e:
        print(e)
        return

# Connect the function to the ChatMemberUpdated event
@app.on_chat_member_updated(filters.group, group=20)
async def member_update_handler(client: app, member: ChatMemberUpdated):
    await handle_member_update(client, member)


