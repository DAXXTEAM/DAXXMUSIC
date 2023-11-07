from pyrogram import Client, filters import requests from bs4 import BeautifulSoup 


@app.on_message(filters.command("bin", prefixes="/") & filters.private)
async def bin_lookup(client, message):
    try:
        bin = message.text.split(" ")[1]
        response = requests.get(f"https://lookup.binlist.net/{bin}")
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
