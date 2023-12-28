from ... import *
from pyrogram import *
from pyrogram.types import *


@app.on_message(filters.command(["gen", "ccgen"], [".", "!", "/"]))
async def gen_cc(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**๏ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ᴀ ʙɪɴ ᴛᴏ\n๏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴄ ...**"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("**ɢᴇɴᴇʀᴀᴛɪɴɢ ...**")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("**❌ ᴡʀᴏɴɢ ʙɪɴ❗...**")
    try:
        resp = await api.ccgen(bin, 10)
        cards = resp.liveCC
        await aux.edit(f"""
**Ⰶ sᴏᴍᴇ ʟɪᴠᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴄ Ⰶ**
`{cards[0]}`\n`{cards[1]}`\n`{cards[2]}`
`{cards[3]}`\n`{cards[4]}`\n`{cards[5]}`
`{cards[6]}`\n`{cards[7]}`\n`{cards[8]}`
`{cards[9]}`
**💳 ʙɪɴ ➠** `{resp.results[0].bin}`
**⏳ ᴛɪᴍᴇ ᴛᴏᴏᴋ ➠** `{resp.took}`\n\n @NYKAAXBOT"""
        )
    except Exception as e:
        return await aux.edit(f"**ᴇʀʀᴏʀ ➠** `{e}`")


