from pyrogram import Client, filters
from pyrogram.types import Message
from pydub import AudioSegment
import os
from DAXXMUSIC import app


@app.on_message(filters.command("dj"))
async def bass_boost_command(client, message):
    try:
        # Check if there is a reply to the command
        if message.reply_to_message and message.reply_to_message.audio:
            original_audio = message.reply_to_message.audio
            file_id = original_audio.file_id

            # Download the audio file
            audio_path = await client.download_media(file_id)

            # Apply bass boost effect
            boosted_audio = apply_bass_boost(audio_path)

            # Send the boosted audio as a reply
            await message.reply_audio(audio=boosted_audio)

            # Clean up temporary files
            os.remove(audio_path)
            os.remove(boosted_audio)

        else:
            await message.reply_text("Please reply to an audio file with /bass to apply the bass boost effect.")
    except Exception as e:
        await message.reply_text(f"🚫")

def apply_bass_boost(audio_path):
    # Load audio file using pydub
    audio = AudioSegment.from_file(audio_path)

    # Apply bass boost effect (adjust the gain according to your preference)
    boosted_audio = audio.low_pass_filter(200).high_pass_filter(70).apply_gain(30)

    # Save the boosted audio as a temporary file
    boosted_audio_path = "yumiboost.mp3"
    boosted_audio.export(boosted_audio_path, format="mp3")

    return boosted_audio_path
