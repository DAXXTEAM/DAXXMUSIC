import asyncio

from pyrogram import filters

import config
from DAXXMUSIC import app
from DAXXMUSIC.misc import SUDOERS
 
from DAXXMUSIC.utils.formatters import convert_bytes





@app.on_message(filters.command(["var"]) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.. Getting your config"
    )
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH

 ##############
 
    text = f"""MUSIC BOT CONFIG:

    
<u>Custom Repo Vars:</u>
UPSTREAM_REPO : {up_r}
UPSTREAM_BRANCH : {up_b}
GITHUB_REPO : {git}
GIT_TOKEN : {token}


    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
