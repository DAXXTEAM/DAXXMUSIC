from pyrogram import Client, filters
from pyrogram.types import Message
import random
from DAXXMUSIC import app

def calculate_love_percentage(name1, name2):
    # Simple random love percentage calculation for demonstration purposes
    return random.randint(1, 100)


@app.on_message(filters.command("love") & filters.regex(r'^/love (.+) (.+)$'))
def love_calculator_command(client, message: Message):
    # Extract names from the command
    names = message.matches[0].groups()
    name1, name2 = names[0], names[1]

    # Calculate love percentage
    love_percentage = calculate_love_percentage(name1, name2)

    # Send the love percentage as a message
    message.reply_text(f"Love Compatibility between {name1} and {name2}: {love_percentage}%")


@app.on_message(filters.command("love") & ~filters.regex(r'^/love (.+) (.+)$'))
def love_calculator_input(client, message: Message):
    # Check if the command has two arguments (names)
    if len(message.command) > 2:
        name1 = message.command[1]
        name2 = message.command[2]

        # Calculate love percentage
        love_percentage = calculate_love_percentage(name1, name2)

        # Send the love percentage as a message
        message.reply_text(f"Love Compatibility between {name1} and {name2}: {love_percentage}%")
