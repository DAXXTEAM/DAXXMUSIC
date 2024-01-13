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

@app.on_message(filters.command("song"))
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("**🔄 sᴇᴀʀᴄʜɪɴɢ... **")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("**⚠️ ɴᴏ ʀᴇsᴜʟᴛs ᴡᴇʀᴇ ғᴏᴜɴᴅ. ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴛʏᴘᴇᴅ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ sᴏɴɢ ɴᴀᴍᴇ**")
        print(str(e))
        return
    m.edit("**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**📤 ᴜᴘʟᴏᴀᴅɪɴɢ...**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}\n**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ {message.from_user.mention}**",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        

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
