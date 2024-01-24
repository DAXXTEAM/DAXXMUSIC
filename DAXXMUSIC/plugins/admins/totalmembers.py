from DAXXMUSIC.utils.daxx_ban import admin_filter
import os
import csv
from pyrogram import Client, filters
from DAXXMUSIC import app

@app.on_message(filters.command("user") & admin_filter)
def user_command(client, message):
    
    chat_members = app.get_chat_members(message.chat.id)

    
    members_list = []
    for member in chat_members:
        members_list.append({
            "username": member.user.username,
            "userid": member.user.id
        })

    
    with open("members.txt", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "userid"])
        writer.writeheader()
        for member in members_list:
            writer.writerow(member)

    # Send the text file as a reply to the message
    app.send_document(message.chat.id, "members.txt")
