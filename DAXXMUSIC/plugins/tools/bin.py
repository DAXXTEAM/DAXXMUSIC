from pyrogram import Client, filters
from pyrogram import types
import requests
from bs4 import BeautifulSoup as bs
from DAXXMUSIC import app


@app.on_message(filters.command('ar'))
def bin_check(client, message):
    try:
        # Extract BIN from the message
        _BIN = message.text[len('/ar '):]

        # Make a request to Binchk API
        _res = requests.get(f'http://binchk-api.vercel.app/bin={_BIN}')
        res = _res.json()

        # Respond with the BIN information
        message.reply_text(f"""
BIN: {_BIN}
Brand⇢ {res["brand"]}
Type⇢ {res["type"]}
Level⇢ {res["level"]}
Bank⇢ {res["bank"]}
Phone⇢ {res["phone"]}
Flag⇢ {res["flag"]}
Currency⇢ {res["currency"]}
Country⇢ {res["country"]}({res["code"]})
""")
    except Exception as e:
        # Handle exceptions, if any
        print(f"Error: {e}")
        message.reply_text("An error occurred while processing your request.")
