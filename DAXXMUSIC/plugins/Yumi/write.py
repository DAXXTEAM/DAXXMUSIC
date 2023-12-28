from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import  BOT_USERNAME
from DAXXMUSIC import app as app
import requests

@app.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "๏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...,\n\n๏ ᴡʀɪᴛɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ...")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
๏ sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘
๏ ᴡʀɪᴛᴛᴇɴ ʙʏ ➛ [ɴʏᴋᴀᴀ](https://t.me/{BOT_USERNAME})
๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➛ {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)

mod_name = "ᴡʀɪᴛᴇᴛᴏᴏʟ"

help = """

 ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /write <ᴛᴇxᴛ> *➛* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
 """
