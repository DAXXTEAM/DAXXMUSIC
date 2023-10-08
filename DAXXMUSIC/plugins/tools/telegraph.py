from telegraph import upload_file
from pyrogram import filters
from DAXXMUSIC import app


@app.on_message(filters.command('tgm'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("🌹𝐌𝐚𝐤𝐢𝐧𝐠 𝐀 𝐋𝐢𝐧𝐤 𝐎𝐟 𝐘𝐨𝐮𝐫 𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭 𝐁𝐚𝐛𝐲....🌹")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'🇾ᴏᴜʀ🇹ᴇʟᴇɢʀᴀᴘʜ 👉 {url}')
