from pyrogram import Client, filters
from pyrogram.types import Message
import random
from DAXXMUSIC import app

def calculate_gay_percentage():
    # Simple random gay percentage calculation for fun
    return random.randint(1, 100)


def generate_gay_response(gay_percentage):
    # Define random texts and emojis for different gay percentage ranges
    if gay_percentage < 30:
        return "You're straight as an arrow. 🏳️‍🌈"
    elif 30 <= gay_percentage < 70:
        return "You might have a bit of a rainbow in you. 🌈"
    else:
        return "You're shining with rainbow colors! 🌟🏳️‍🌈"

@app.on_message(filters.command("gay") & filters.regex(r'^/gay$'))
def gay_calculator_command(client, message: Message):
    # Calculate gay percentage
    gay_percentage = calculate_gay_percentage()

    # Generate gay response
    gay_response = generate_gay_response(gay_percentage)

    # Send the gay response as a message
    message.reply_text(f"Gay Percentage: {gay_percentage}%\n{gay_response}")
