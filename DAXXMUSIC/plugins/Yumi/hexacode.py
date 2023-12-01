from pyrogram import Client, filters
from DAXXMUSIC import app



def text_to_hex(text):
    hex_representation = ' '.join(format(ord(char), 'x') for char in text)
    return hex_representation





@app.on_message(filters.command("code"))
def ascii_to_hex_command(_, message):
    if len(message.command) > 1:
        original_text = " ".join(message.command[1:])
        hex_representation = text_to_hex(original_text)

        response_text = f"Original Text: {original_text}\nHex Representation: {hex_representation}"

        message.reply_text(response_text)
    else:
        message.reply_text("Please provide text after the /code command.")
