from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.utils import bot_sys_stats
from DAXXMUSIC.utils.decorators.language import language
from DAXXMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL
import aiohttp
from io import BytesIO
from DAXXMUSIC import app
from pyrogram import filters



async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    pytgping = await DAXX.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    await message.reply_photo(carbon)
    await text.delete()
