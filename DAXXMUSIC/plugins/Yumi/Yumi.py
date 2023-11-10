from lexica import Client
from pyrogram import filters
from DAXXMUSIC import DAXX




def main(prompt: str) -> str:
    client = Client()
    response = client.palm(prompt)
    return response["content"].strip()

@DAXX.on_message(filters.regex(r"Y|y|b|B"))
async def deepchat(zuli: Zuli, message):
    if message.reply_to_message:
        query = message.text.split(' ', 1)[1]
        x = main(query)
        await message.reply(x)
    else:
        query = message.text.split(' ', 1)[1]
        x = main(query)
        await message.reply(x)
