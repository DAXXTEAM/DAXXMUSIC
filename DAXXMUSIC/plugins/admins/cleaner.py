import os
from DAXXMUSIC import app
from pyrogram import filters
from pyrogram.types import Message



downloads_directory = os.path.join("DAXXMUSIC", "Helper", "downloader", "downloads")
raw_directory = os.path.join("DAXXMUSIC", "Helper", "downloader", "raw_files")


@app.on_message(filters.command(["rmd", "clear"], prefixes=["/", "!"]))
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads_directory)
    if ls_dir:
        for file in os.listdir(downloads_directory):
            os.remove(os.path.join(downloads_directory, file))
        await message.reply_text("✅ ᴅᴇʟᴇᴛᴇᴅ ᴀʟʟ ᴅᴏᴡɴʟᴏᴀᴅ ғɪʟᴇs.")
    else:
        await message.reply_text("❌ ɴᴏ ғɪʟᴇs ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ")


@app.on_message(filters.command(["rmw", "clean"], prefixes=["/", "!"]))
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_directory)
    if ls_dir:
        for file in os.listdir(raw_directory):
            os.remove(os.path.join(raw_directory, file))
        await message.reply_text("✅ ᴅᴇʟᴇᴛᴇᴅ ᴀʟʟ ʀᴀᴡ ғɪʟᴇs.")
    else:
        await message.reply_text("❌ ɴᴏ ʀᴀᴡ ғɪʟᴇs.")
