from ... import *
from pyrogram import *
from pyrogram.types import *

from pyrogram import Client, filters
from DAXXMUSIC import app



def fetch_cc_info(bin_number):
    cc_api_url = f"https://api.safone.dev/ccgen?bins={bin_number}"
    response = app.get(cc_api_url)
    if response.ok:
        cc_data = response.json()
        cc_info = f"Generated Credit Card Info:\n\nCard Number: {cc_data.get('credit_card_number')}\nCard Type: {cc_data.get('card_type')}\nCard Holder: {cc_data.get('card_holder')}\nExpiration Date: {cc_data.get('expiration_date')}"
        return cc_info
    else:
        return "Failed to fetch credit card information"


@app.on_message(filters.command("ccgen"))
def ccgen_command(client, message):
    text = message.text.split(" ", 1)
    if len(text) > 1:
        bin_number = text[1]
        cc_info = fetch_cc_info(bin_number)
        message.reply_text(cc_info)
    else:
        message.reply_text("Please provide a BIN (Bank Identification Number) after the command.")
