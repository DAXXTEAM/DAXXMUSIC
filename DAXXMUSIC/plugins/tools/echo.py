from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC.utils.daxx_ban import admin_filter
from DAXXMUSIC import app
from DAXXMUSIC.misc import SUDOERS
echo_status = {}


@app.on_message(filters.command("echo") & filters.group & admin_filter & SUDOERS)
async def toggle_echo(client, message):
    chat_id = message.chat.id
    if chat_id not in echo_status:
        echo_status[chat_id] = False

    if len(message.command) > 1:
        status = message.command[1].lower()
        if status == "on":
            echo_status[chat_id] = True
            await message.reply("Echo is now enabled!")
        elif status == "off":
            echo_status[chat_id] = False
            await message.reply("Echo is now disabled!")
        else:
            await message.reply("Invalid command! Use /echo on or /echo off.")
    else:
        await message.reply("Invalid command! Use /echo on or /echo off.")


@app.on_message(filters.group & ~filters.bot)
async def echo(client, message):
    chat_id = message.chat.id
    if chat_id in echo_status and echo_status[chat_id]:
        await message.reply(message.text)

