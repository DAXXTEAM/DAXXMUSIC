from io import BytesIO
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.raw.base import InputFile
from DAXXMUSIC import app


@app.on_message(filters.command("mmf") & filters.reply)
async def memify_handler(client, message):
    if not message.reply_to_message or not message.reply_to_message.media:
        await message.reply("Reply to an image/sticker.")
        return

    file_info = message.reply_to_message.document or message.reply_to_message.photo
    file_path = await message.reply_to_message.download(file_name="temp")

    text = message.text.split("/mmf", maxsplit=1)[1].strip()

    if not text:
        await message.reply("Provide some text to memify!")
        return

    await message.reply("Memifying this image! ✊🏻")

    memified_file = await create_memified_image(file_path, text)

    output_bytes_io = BytesIO(memified_file)

    await client.send_document(
        chat_id=message.chat.id,
        document=InputFile(output_bytes_io, filename="memified_image.webp"),
        caption="Here is your memified image!",
    )

    os.remove(file_path)
    os.remove("memified_image.webp")

async def create_memified_image(image_path, text):
    img = Image.open(image_path)

    i_width, i_height = img.size

    font_path = "./DAXXMUSIC/assets/font2.ttf" if os.name == "nt" else "./DAXXMUSIC/assets/font.ttf"
    font_size = int((70 / 640) * i_width)
    font = ImageFont.truetype(font_path, font_size)

    draw = ImageDraw.Draw(img)
    pad = 5

    await draw_text_lines(draw, text, font, i_width, i_height, pad)

    output = BytesIO()
    img.save(output, format="WEBP")

    return output.getvalue()

async def draw_text_lines(draw, text, font, i_width, i_height, pad):
    current_h = i_height // 2

    for line in textwrap.wrap(text, width=15):
        text_width, text_height = draw.textsize(line, font=font)

        for offset in [(-2, 0), (2, 0), (0, -2), (0, 2), (0, 0)]:
            draw.text(
                xy=(
                    ((i_width - text_width) / 2) + offset[0],
                    current_h + offset[1],
                ),
                text=line,
                font=font,
                fill=(0, 0, 0),
            )

        draw.text(
            xy=((i_width - text_width) / 2, current_h),
            text=line,
            font=font,
            fill=(255, 255, 255),
        )

        current_h += text_height + pad
