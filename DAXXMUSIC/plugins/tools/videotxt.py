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
    
    