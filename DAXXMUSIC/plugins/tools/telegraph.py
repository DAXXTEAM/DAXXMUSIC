from telegraph import upload_file
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "link"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' 🇾ᴏᴜʀ🇹ᴇʟᴇɢʀᴀᴘʜ {url}')

#######
@app.on_message(filters.command("wall"))
async def wall(_, message: Message):
    " ғɪxᴇᴅ ᴡᴀʟʟ ʙʏ ᴍᴜᴋᴇsʜ"
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None
    if not text:
        return await message.reply_text("Please give some query to search.")
    m = await message.reply_text("Searching for wallpapers...")
    try:
        url = requests.get(f"https://api.safone.me/wall?query={text}").json()["results"]
        ran = random.randint(0, 3)
        await message.reply_photo(
            photo=url[ran]["imageUrl"],
            caption=f"🥀 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ʟɪɴᴋ", url=url[ran]["imageUrl"])],
                ]
            ),
        )
        await m.delete()
    except Exception as e:
        await m.edit_text(
            f"ᴡᴀʟʟᴘᴀᴘᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ : {text}`",
        )
