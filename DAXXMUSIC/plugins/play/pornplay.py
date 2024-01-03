from pyrogram import filters
import requests, random
from bs4 import BeautifulSoup
from DAXXMUSIC import app
import pytgcalls
import os, yt_dlp 
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls.types import AudioVideoPiped


#


async def get_video_stream(link):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
    x = yt_dlp.YoutubeDL(ydl_opts)
    info = x.extract_info(link, False)
    video = os.path.join(
        "downloads", f"{info['id']}.{info['ext']}"
    )
    if os.path.exists(video):
        return video
    x.download([link])
    return video







def get_video_info(title):
    url_base = f'https://www.xnxx.com/search/{title}'
    try:
        with requests.Session() as s:
            r = s.get(url_base)
            soup = BeautifulSoup(r.text, "html.parser")
            video_list = soup.findAll('div', attrs={'class': 'thumb-block'})
            if video_list:
                random_video = random.choice(video_list)
                thumbnail = random_video.find('div', class_="thumb").find('img').get("src")
                if thumbnail:
                    # Replace the size in the thumbnail URL to get 500x500
                    thumbnail_500 = thumbnail.replace('/h', '/m').replace('/1.jpg', '/3.jpg')
                    link = random_video.find('div', class_="thumb-under").find('a').get("href")
                    if link and 'https://' not in link:
                        return {'link': 'https://www.xnxx.com' + link, 'thumbnail': thumbnail_500}
    except Exception as e:
        print(f"Error: {e}")
    return None


button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ᴘʟᴀʏ",callback_data="pplay_data"),
            InlineKeyboardButton("ᴄʟᴏsᴇ",callback_data="close_data")
        ]
    ])


@app.on_message(filters.command("porn"))
async def get_random_video_info(client, message):
    if len(message.command) == 1:
        await message.reply("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴛɪᴛʟᴇ ᴛᴏ sᴇᴀʀᴄʜ.")
        return

    title = ' '.join(message.command[1:])
    msg = await message.reply("processing...")
    video_info = get_video_info(title)
    
    if video_info:
        video_link = video_info['link']
        await msg.edit("download your video....")
        video = await get_video_stream(video_link)
        await msg.edit("uploading your video....")
        await message.reply_video(video, caption=f"{title}", reply_markup=button)
        await msg.delete()     
    else:
        await message.reply(f"Nᴏ ᴠɪᴅᴇᴏ ʟɪɴᴋ ғᴏᴜɴᴅ ғᴏʀ '{title}'.")



@app.on_callback_query(filters.regex(r"pplay_data"))
async def porn_play(_, query):
    chat_id = query.message.chat.id
    await query.answer("Playing, give me time...")

    if query.message.reply_to_message and query.message.reply_to_message.video:
        msg = await query.message.reply("Processing")
        video_path = await query.message.reply_to_message.download()

        await pytgcalls.join_group_call(
            chat_id,
            AudioVideoPiped(video_path),
        )

        await query.message.reply("Nᴏᴡ ᴘʟᴀʏ ᴠɪᴅᴇᴏ")
    else:
        await query.message.reply("Invalid request!")



@app.on_message(filters.command("pornplay"))
async def get_random_video_info(client, message):
    chat_id = message.chat.id
    if len(message.command) == 1:
        await message.reply("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴛɪᴛʟᴇ ᴛᴏ sᴇᴀʀᴄʜ.")
        return

    title = ' '.join(message.command[1:])
    msg = await message.reply("processing...")
    video_info = get_video_info(title)
    
    if video_info:
        video_link = video_info['link']
        await msg.edit("ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴡᴀɪᴛ sᴏᴍᴇ ᴛɪᴍᴇ....")
        video_path = await get_video_stream(video_link)
        await msg.edit("ᴜᴘʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ᴠɪᴅᴇᴏ....")
        await pytgcalls.join_group_call(
            chat_id,
            AudioVideoPiped(video_path),
        )
        await msg.delete()     
        await message.reply("Nᴏᴡ ᴘʟᴀʏ ᴠɪᴅᴇᴏ")
        
    else:
        await message.reply(f"Nᴏ ᴠɪᴅᴇᴏ ʟɪɴᴋ ғᴏᴜɴᴅ ғᴏʀ '{title}'.")