import os
import cv2
from PIL import Image
from pyrogram import Client, filters
from DAXXMUSIC import app


@app.on_message(filters.command("tiny"))
async def tiny_sticker(client, message):
    reply = message.reply_to_message
    if not (reply and reply.sticker):
        await message.reply("Please reply to a sticker")
        return
    kontol = await message.reply("Processing please wait")
    await kontol.edit_text("🐾")
    ik = await app.download_media(reply)
    im1 = Image.open("DAXXMUSIC/assets/mohit.png")
    if ik.endswith(".tgs"):
        await app.download_media(reply, "wel2.tgs")
        os.system("lottie_convert.py wel2.tgs json.json")
        with open("json.json", "r") as json_file:
            jsn = json_file.read()
            jsn = jsn.replace("512", "2000")
        with open("json.json", "w") as json_file:
            json_file.write(jsn)
        os.system("lottie_convert.py json.json wel2.tgs")
        file = "wel2.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        _, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await app.send_document(message.chat.id, file, reply_to_message_id=message.id)
    await kontol.delete()
    os.remove(file)
    os.remove(ik)
