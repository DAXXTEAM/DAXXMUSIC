from ... import *
from pyrogram import *
from pyrogram.types import *


@app.on_message(filters.command(["bin", "ccbin", "bininfo"]))
async def check_ccbin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**Please Give Me a Bin To\nGet Bin Details !**"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("**Checking ...**")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("**❌ Wrong Bin❗...**")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
**💠 Bin Full Details:**

**🏦 Bank:** `{resp.bank}`
**💳 Bin:** `{resp.bin}`
**🏡 Country:** `{resp.country}`
**🇮🇳 Flag:** `{resp.flag}`
**🧿 ISO:** `{resp.iso}`
**⏳ Level:** `{resp.level}`
**🔴 Prepaid:** `{resp.prepaid}`
**🆔 Type:** `{resp.type}`
**ℹ️ Vendor:** `{resp.vendor}`"""
        )
    except Exception as e:
        return await aux.edit(f"**Error:** `{e}`")
      
