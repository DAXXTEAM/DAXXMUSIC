from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC import app

CRICKET_API_URL = "https://sugoi-api.vercel.app/cricket"
FOOTBALL_API_URL = "https://sugoi-api.vercel.app/football"

async def get_match_text(match, sport):
    match_text = f"{'🏏' if sport == 'cricket' else '⚽️'} **{match['title']}**\n\n"
    match_text += f"🗓 *Date:* {match['date']}\n"
    match_text += f"🏆 *Team 1:* {match['team1']}\n"
    match_text += f"🏆 *Team 2:* {match['team2']}\n"
    match_text += f"🏟️ *Venue:* {match['venue']}"
    return match_text

def create_inline_keyboard(sport):
    inline_keyboard = [
        [
            InlineKeyboardButton(
                f"Next {sport.capitalize()} Match ➡️",
                callback_data=f"next_{sport}_match",
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard)

# 

@app.on_message(filters.command("cricket"))
async def get_cricket_match(_, message):
    try:
        response = requests.get(CRICKET_API_URL)
        match_data = response.json()
        match_text = await get_match_text(match_data, "cricket")
        keyboard = create_inline_keyboard("cricket")
        await message.reply_text(match_text, reply_markup=keyboard, parse_mode="markdown")
    except Exception as e:
        print("Error fetching cricket match:", str(e))
        await message.reply_text("Error fetching cricket match details.")

# Command to fetch football match details
@app.on_message(filters.command("football"))
async def get_football_match(_, message):
    try:
        response = requests.get(FOOTBALL_API_URL)
        match_data = response.json()
        match_text = await get_match_text(match_data, "football")
        keyboard = create_inline_keyboard("football")
        await message.reply_text(match_text, reply_markup=keyboard, parse_mode="markdown")
    except Exception as e:
        print("Error fetching football match:", str(e))
        await message.reply_text("Error fetching football match details.")

# Callback query handler for inline keyboards
@app.on_callback_query()
async def on_inline_button_clicked(_, callback_query):
    sport = callback_query.data.split("_")[1]
    # Handle the callback based on the sport (cricket or football)
    await callback_query.answer(f"Fetching next {sport.capitalize()} match...")

#
