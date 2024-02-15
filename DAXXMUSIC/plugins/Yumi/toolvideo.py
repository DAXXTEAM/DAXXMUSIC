import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pydub import AudioSegment
import speech_recognition as sr
from DAXXMUSIC import app
# --------------------------------------

def convert_video_to_text(video_path):
    audio = AudioSegment.from_file(video_path)
    audio.export("audio.wav", format="wav")
# -----------------------------------------
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        audio_data = recognizer.record(source)
# --------------------------------------------
    text = recognizer.recognize_google(audio_data)
    return text

# ----------------------------------------------

@app.on_message(filters.command("vtxt") & filters.reply)
def convert_video_to_text_cmd(_, message: Message):
    # -------------------------------
    video_path = message.reply_to_message.download("video.mp4")

    # ------------------------------
    text_result = convert_video_to_text(video_path)

    # --------------------------
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write(text_result)
     # ---------------------------   
    message.reply_document("file.txt")
    
    
    
    # -------------------------------------
    
@app.on_message(filters.command("remove", prefixes="/") & filters.reply)
def remove_media(client, message: Message):
    # Fetching the replied message
    replied_message = message.reply_to_message

    if replied_message.video:
        # If the replied message is a video, remove either the audio or the video depending on the command
        if len(message.command) > 1:
            command = message.command[1].lower()
            if command == "audio":
                # Remove audio
                file_path = app.download_media(replied_message.video)
                audio = AudioSegment.from_file(file_path)
                audio = audio.set_channels(1)
                audio.export("output.mp3", format="mp3")
                app.send_audio(message.chat.id, "output.mp3")
                os.remove(file_path)
                os.remove("output.mp3")
            elif command == "video":
                # Remove video
                file_path = app.download_media(replied_message.video)
                os.system(f"ffmpeg -i {file_path} -c copy -an output.mp4")
                app.send_video(message.chat.id, "output.mp4")
                os.remove(file_path)
                os.remove("output.mp4")
            else:
                app.send_message(message.chat.id, "Invalid command. Please use either /remove audio or /remove video.")
        else:
            app.send_message(message.chat.id, "Please specify whether to remove audio or video using /remove audio or /remove video.")
    else:
        app.send_message(message.chat.id, "The replied message is not a video.")
        
