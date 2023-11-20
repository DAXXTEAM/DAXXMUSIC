import logging
import os
from datetime import datetime

from pyrogram import Client, filters

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

from DAXXMUSIC import app

async def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )

@app.on_message(filters.command("pt") | filters.private)
async def paste(event):
    if event.forward_from:
        return
    datetime.now()
    if not os.path.isdir(bot.get_config("TMP_DOWNLOAD_DIRECTORY")):
        os.makedirs(bot.get_config("TMP_DOWNLOAD_DIRECTORY"))
    input_str = event.text.split(" ", maxsplit=1)[1] if len(event.text.split(" ", maxsplit=1)) > 1 else None
    if input_str:
        message = input_str
    elif event.reply_to_message:
        previous_message = event.reply_to_message
        if previous_message.media:
            downloaded_file_name = await bot.download_media(
                previous_message,
                bot.get_config("TMP_DOWNLOAD_DIRECTORY"),
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = previous_message.text
    else:
        await event.edit("Give Some Text Or File To Paste")
        return
    py_file = ""
    name = "ok"
    if previous_message.media:
        name = await app.download_media(
            previous_message,
            bot.get_config("TMP_DOWNLOAD_DIRECTORY"),
            progress_callback=progress,
        )
    downloaded_file_name = name
    if downloaded_file_name.endswith(".py"):
        py_file += ".py"
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}{py_file}"
        raw = f"https://nekobin.com/raw/{key}{py_file}"
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
        await event.edit(reply_text)
    else:
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        raw = f"https://nekobin.com/raw/{key}"
        reply_text = f"Pasted Text [neko]({url})\n Raw ? [View Raw]({raw})"
        await event.edit(reply_text)
