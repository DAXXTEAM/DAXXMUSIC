from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#
@app.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇────────────────────────────────────◇ 
  
@app.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logohq?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇──────────────────────────────────────◇ 


@app.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/wallpaper?search={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 Open In Google 🍀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )


logo.run()

app.start()
LOGGER.info("@iam_daxx")
idle()
