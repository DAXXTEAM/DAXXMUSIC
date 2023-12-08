import pyrogram
import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency):
    try:
        conversion_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(conversion_url)
        data = response.json()
        rates = data["rates"]
        
        if from_currency != "USD":
            amount_in_usd = amount / rates[from_currency]
        else:
            amount_in_usd = amount
        
        if to_currency == "USD":
            converted_amount = amount_in_usd
        else:
            converted_amount = amount_in_usd * rates[to_currency]
        
        return converted_amount
    except Exception as e:
        print("Error performing currency conversion:", e)
        return "Error performing currency conversion."

# Handler for the /cn command
@app.on_message(pyrogram.filters.command("cn"))
def currency_converter(bot, update):
    text = update.text
    match = re.match(r'/cn (\d+(\.\d+)?) (\w+) TO (\w+)', text)
    
    if match:
        amount = float(match.group(1))
        from_currency = match.group(3).upper()
        to_currency = match.group(4).upper()
        
        converted_amount = convert_currency(amount, from_currency, to_currency)
        
        update.reply_text(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        update.reply_text("Invalid command format. Use `/cn 1 USD TO INR` ")
