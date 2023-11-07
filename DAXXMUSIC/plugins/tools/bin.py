from pyrogram import Client, filters
import requests
from DAXXMUSIC import DAXX

headers = {
    'apikey': "xQ67Pt1toQt2RskCPFUF82J2lCYrj8c2",
}

@app.on_message(filters.command("binn", prefixes="/") & filters.private)
async def bin_lookup(client, message):
    try:
        bin = message.text.split(" ")[1]
        response = requests.get(f"https://api.apilayer.com/bincheck/{bin}", headers=headers)
        if response.status_code == 200:
            data = response.json()
            bank = data.get("bank", {}).get("name", "N/A")
            name = data.get("name", "N/A")
            brand = data.get("brand", "N/A")
            country = data.get("country", {}).get("name", "N/A")
            scheme = data.get("scheme", "N/A")
            emoji = data.get("emoji", "❌")
            card_type = data.get("type", "N/A")

            result_message = (
                f"🔍 BIN Lookup\n"
                f"BIN: {bin}\n"
                f"Bank: {bank}\n"
                f"Name: {name}\n"
                f"Brand: {brand}\n"
                f"Country: {country} {emoji}\n"
                f"Scheme: {scheme}\n"
                f"Type: {card_type}"
            )
        else:
            result_message = "❌ BIN Lookup Failed"

        await message.reply_text(result_message, parse_mode="markdown")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
