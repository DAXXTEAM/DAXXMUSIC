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

#image

@app.on_message(filters.command(["image", "generate", "photo"]))
async def pinterest(_, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍")

     images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

     media_group = []
     count = 0

     msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
     for url in images["images"][:6]:
                  
          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

     try:
        
        await DAXXMUSIC.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")
         
@app.on_message(filters.command(["chichi"]))
async def pinterest(_, message):
    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    response = requests.get(f"https://nova-api-seven.vercel.app/api/images?name={query}")
    image_data = response.json()
    msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ chichi...") 
    image_urls = image_data.get("image_urls", [])

    images = []
    max_images = 10
    for i, url in enumerate(image_urls):
        if i >= max_images:
            break
                
        image = InputMediaPhoto(url)
        images.append(image)

    media_groups = [images[i:i + 10] for i in range(0, len(images), 10)]

    for media_group in media_groups:
         try:
              await DAXXMUSIC.send_media_group(message.chat.id, media=media_group)
              return await msg.delete()
         except Exception as e:
              await msg.delete()
              return await message.reply(f"ᴇʀʀᴏʀ : {e}")
