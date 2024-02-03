import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pydub import AudioSegment
import tempfile
import yt_dlp
from DAXXMUSIC import app

yt_dl = yt_dlp.YoutubeDL()

@app.on_message(filters.command("bass"))
async def bass_boost_command(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.audio:
            original_audio = message.reply_to_message.audio
            file_id = original_audio.file_id

            audio_path = await client.download_media(file_id)

            boosted_audio = apply_bass_boost(audio_path)

            await message.reply_audio(audio=boosted_audio)

            os.remove(audio_path)
            os.remove(boosted_audio)

        else:
            await message.reply_text("Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴡɪᴛʜ /ʙᴀss ᴛᴏ ᴀᴘᴘʟʏ ᴛʜᴇ ʙᴀss ʙᴏᴏsᴛ ᴇғғᴇᴄᴛ")
    except Exception as e:
        await message.reply_text(f"🚫")


def apply_bass_boost(audio_path):
    audio = AudioSegment.from_file(audio_path)

    
    boosted_audio = (
        audio
        .low_pass_filter(180)
        .high_pass_filter(38)
        .apply_gain(14)
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        boosted_audio.export(temp_file.name, format="mp3")
        boosted_audio_path = temp_file.name

    return boosted_audio_path
