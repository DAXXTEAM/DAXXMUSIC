from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC import app 

# Command to generate a direct WhatsApp link
@app.on_message(filters.command("WhatsApp"))
async def generate_whatsapp_link(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please enter your phone number after the command. Example: /WhatsApp +1234567890")
        return

    phone_number = message.command[1]

    # Generate the WhatsApp link
    whatsapp_link = f"https://wa.me/{phone_number}"

    await message.reply(f"Click the link to open WhatsApp with the number {phone_number}:\n{whatsapp_link}")
