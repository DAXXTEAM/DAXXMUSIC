from pyrogram import Client, filters
from pyrogram import types
import requests
from bs4 import BeautifulSoup as bs
from DAXXMUSIC import app

# Function to handle /da command
@app.on_message(filters.command('bin'))
def bin_check(client, message):
    try:
        # Extract BIN from the message
        _BIN = message.text[len('/bin '):]

        # Make a request to Binchk API
        _res = requests.get(f'http://binchk-api.vercel.app/bin={_BIN}')
        res = _res.json()

        # Respond with the BIN information
        message.reply_text(f'''
𝗕𝗜𝗡: `{_BIN}`
𝗕𝗿𝗮𝗻𝗱⇢ **{res["brand"]}**
𝗧𝗬𝗣𝗘⇢ **{res["type"]}**
𝗟𝗘𝗩𝗘𝗟⇢ **{res["level"]}**
𝗕𝗔𝗡𝗞⇢ **{res["bank"]}**
𝗣𝗛𝗢𝗡𝗘⇢ **{res["phone"]}**
𝗙𝗟𝗔𝗚⇢ **{res["flag"]}**
𝗖𝗨𝗥𝗥𝗘𝗡𝗖𝗬⇢ **{res["currency"]}**
𝗖𝗢𝗨𝗡𝗧𝗬⇢ **{res["country"]}({res["code"]})**
''')
    except Exception as e:
        # Handle exceptions, if any
        print(f"""Please Give Me a Bin To
Get Bin Details""")
        message.reply_text("""🚫 Incorrect input. Please provide a 6-digit BIN number.""")
