import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC import app

action_info = {
    "kiss": {"api": "https://api.waifu.pics/sfw/kiss", "emoji": "😘"},
    "slap": {"api": "https://api.waifu.pics/sfw/slap", "emoji": "😒"},
}

def handle_action(client, message: Message, action: str, action_name: str):
    sender = message.from_user
    sender_name = f"[{sender.first_name}](tg://user?id={sender.id})" 

    if message.reply_to_message:
        replied_user = message.reply_to_message.from_user
        replied_user_name = f"[{replied_user.first_name}](tg://user?id={replied_user.id})"
        msg = f"{sender_name} sent a {action_name} to {replied_user_name}! {action_info[action]['emoji']}"
    else:
        msg = f"{sender_name} sent a {action_name} to themselves! {action_info[action]['emoji']}"

    response = requests.get(action_info[action]['api'])
    if response.status_code == 200:
        gif_link = response.json()["url"]
        app.send_animation(message.chat.id, animation=gif_link, caption=msg, parse_mode="markdown")

@app.on_message(filters.command("kiss"))
def kiss_command(client, message):
    handle_action(client, message, "kiss", "kiss")

@app.on_message(filters.command("slap"))
def slap_command(client, message):
    handle_action(client, message, "slap", "slap")
