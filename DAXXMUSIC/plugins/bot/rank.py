from pyrogram import Client, filters
from collections import defaultdict
from DAXXMUSIC import app


# This dictionary will hold the count of messages per user
message_counts = defaultdict(int)

#
@app.on_message(filters.group)
async def message_counter(client, message):
    user_id = message.from_user.id
    message_counts[user_id] += 1

@app.on_message(filters.command("rank") & filters.group)
async def send_ranking(client, message):
    # Sort users by message count in descending order
    sorted_counts = dict(sorted(message_counts.items(), key=lambda item: item[1], reverse=True))
    
    ranking_text = "Message Ranking:\n\n"
    for user_id, count in sorted_counts.items():
        try:
            user = await app.get_users(user_id)  # Get user info
            name = user.first_name
            ranking_text += f"{name} - {count} messages\n"
        except Exception as e:
            ranking_text += f"UserID {user_id} - {count} messages\n"

    await message.reply(ranking_text)