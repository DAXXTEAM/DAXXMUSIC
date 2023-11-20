import codecs
import os
import requests
from pyrogram import Client 
from DAXXMUSIC import app 


@app.on_message(filters.command("pt"))

async def paste(_, message):
    if message.reply_to_message:
        if message.reply_to_message.document:
            file = await app.get_file(message.reply_to_message.document.file_id)
            file.download("file.txt")
            text = codecs.open("file.txt", "r+", encoding="utf-8")
            paste_text = text.read()
        else:
            paste_text = message.reply_to_message.text
    else:
        await message.reply_text("What am I supposed to do with this?")
        return

    try:
        link = (
            requests.post(
                "https://nekobin.com/api/documents",
                json={"content": paste_text},
            )
            .json()
            .get("result")
            .get("key")
        )
        text = "Pasted to Nekobin!!!"
        buttons = [
            [
                InlineKeyboardButton(
                    text="View Link", url=f"https://nekobin.com/{link}"
                ),
                InlineKeyboardButton(
                    text="View Raw",
                    url=f"https://nekobin.com/raw/{link}",
                ),
            ]
        ]
        await message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
        os.remove("file.txt")
    except Exception as excp:
        await message.reply_text(f"Failed. Error: {excp}")
        return
