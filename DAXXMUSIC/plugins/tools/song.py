import os
import asyncio
import yt_dlp
import requests
import os
import asyncio
import requests
import wget
import yt_dlp
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from DAXXMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["song"], ["/", "!", "."]))
async def song(client: Client, message):
    aux = await message.reply_text("** ■□□□□□□□□□ 10%**")
    if len(message.command) < 2:
        return await aux.edit(
            "**🤖 𝐆𝐢𝐯𝐞 🙃 𝐌𝐮𝐬𝐢𝐜 💿 𝐍𝐚𝐦𝐞 😍\n💞 𝐓𝐨 🔊 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 🥀 𝐒𝐨𝐧𝐠❗**"
        )
    try:
        song_name = message.text.split(None, 1)[1]
        vid = VideosSearch(song_name, limit=1)
        song_results = vid.result()
        if song_results:
            song_title = song_results["result"][0]["title"]
            song_link = song_results["result"][0]["link"]
        else:
            return await aux.edit("**No results found for the given song name.**")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"downloads/{song_title}.mp3",
            "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
        }
        await aux.edit("**■■■■■□□□□□ 50%**")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_link])  # Pass song_link as a list
        await aux.edit("**■■■■■■■■■□ 90%**")
        audio_path = f"downloads/{song_title}.mp3"
        if os.path.exists(audio_path):
            await message.reply_audio(audio_path)
            os.remove(audio_path)
        else:
            await aux.edit("**Failed to download the audio.**")
        await aux.delete()
    except Exception as e:
        await aux.edit(f"**Error:** {e}")

# ------------------------------------------------------------------------------- #

###### INSTAGRAM REELS DOWNLOAD


@app.on_message(filters.command(["ig"], ["/", "!", "."]))
async def download_instareels(c: app, m: Message):
    try:
        reel_ = m.command[1]
    except IndexError:
        await m.reply_text("Give me an link to download it...")
        return
    if not reel_.startswith("https://www.instagram.com/reel/"):
        await m.reply_text("In order to obtain the requested reel, a valid link is necessary. Kindly provide me with the required link.")
        return
    OwO = reel_.split(".",1)
    Reel_ = ".dd".join(OwO)
    try:
        await m.reply_video(Reel_)
        return
    except Exception:
        try:
            await m.reply_photo(Reel_)
            return
        except Exception:
            try:
                await m.reply_document(Reel_)
                return
            except Exception:
                await m.reply_text("I am unable to reach to this reel.")



######

@app.on_message(filters.command(["reel"], ["/", "!", "."]))
async def instagram_reel(client, message):
    if len(message.command) == 2:
        url = message.command[1]
        response = requests.post(f"https://lexica-api.vercel.app/download/instagram?url={url}")
        data = response.json()

        if data['code'] == 2:
            media_urls = data['content']['mediaUrls']
            if media_urls:
                video_url = media_urls[0]['url']
                await message.reply_video(f"{video_url}")
            else:
                await message.reply("No video found in the response. may be accountbis private.")
        else:
            await message.reply("Request was not successful.")
    else:
        await message.reply("Please provide a valid Instagram URL using the /reels command.")
