import asyncio, os, time, aiohttp
from pathlib import Path
from blackpink import blackpink as bp
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from DAXXMUSIC import app

####
button = InlineKeyboardMarkup([[
            InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close_data")
                              ]])
#####

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

#####

@app.on_message(filters.command("blackpink"))
async def blackpink(_, message):
    text = message.text[len("/blackpink ") :]
    bp(f"{text}").save(f"blackpink_{message.from_user.id}.png")
    await message.reply_photo(f"blackpink_{message.from_user.id}.png", reply_markup=button)
    os.remove(f"blackpink_{message.from_user.id}.png")
