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

<u>Basic Vars:</u>
MUSIC_BOT_NAME : {bot_name}
DURATION_LIMIT : {play_duration} min
SONG_DOWNLOAD_DURATION_LIMIT : {song} min
OWNER_ID : {owner_id}
    
<u>Custom Repo Vars:</u>
UPSTREAM_REPO : {up_r}
UPSTREAM_BRANCH : {up_b}
GITHUB_REPO : {git}
GIT_TOKEN : {token}


<u>Bot Vars:</u>
AUTO_LEAVING_ASSISTANT : {ass}
ASSISTANT_LEAVE_TIME : {auto_leave} seconds
AUTO_SUGGESTION_MODE : {a_sug}
AUTO_SUGGESTION_TIME : {auto_sug} seconds
AUTO_DOWNLOADS_CLEAR : {down}
PRIVATE_BOT_MODE : {pvt}
YOUTUBE_EDIT_SLEEP : {yt_sleep} seconds
TELEGRAM_EDIT_SLEEP : {tg_sleep} seconds
CLEANMODE_MINS : {cm} mins
VIDEO_STREAM_LIMIT : {v_limit} chats
SERVER_PLAYLIST_LIMIT : {playlist_limit}
PLAYLIST_FETCH_LIMIT : {fetch_playlist}

<u>Spotify Vars:</u>
SPOTIFY_CLIENT_ID : {sotify}
SPOTIFY_CLIENT_SECRET : {sotify}

<u>Playsize Vars:</u>
TG_AUDIO_FILESIZE_LIMIT : {tg_aud}
TG_VIDEO_FILESIZE_LIMIT : {tg_vid}

<u>URL Vars:</u>
SUPPORT_CHANNEL : {s_c}
SUPPORT_GROUP :  {s_g}
START_IMG_URL :  {start}
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
