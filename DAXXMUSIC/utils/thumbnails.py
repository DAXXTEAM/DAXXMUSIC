import os
import re
import random
import textwrap
import aiofiles
import aiohttp

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch

from DAXXMUSIC import app
from config import YOUTUBE_IMG_URL, BOT_NAME


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def clear(text):
    words = text.split(" ")
    title = ""
    for word in words:
        if len(title) + len(word) < 60:
            title += " " + word
    return title.strip()


async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        
        # Check if the 'filter' attribute is available in the Image module
        if hasattr(Image, 'filter'):
            background = image2.filter(filter=ImageFilter.BoxBlur(50))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.9)
        else:
            # If 'filter' attribute is not available, use a different approach for blurring
            background = image2.filter(ImageFilter.BoxBlur(50))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.9)
        
        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo = ImageOps.expand(logo, border=17, fill="pink")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        
        # Adjust the font size here
        font_size = 40
        font = ImageFont.truetype("DAXXMUSIC/assets/font2.ttf", font_size)
        font2_size = 70
        font2 = ImageFont.truetype("DAXXMUSIC/assets/font2.ttf", font2_size)
        arial = ImageFont.truetype("DAXXMUSIC/assets/font2.ttf", 30)
        name_font = ImageFont.truetype("DAXXMUSIC/assets/font.ttf", 40)
        
        para = textwrap.wrap(clear(title), width=32) 
        j = 0
        draw.text(
            (6, 6), f"{BOT_NAME}", fill="Yellow", font=name_font
        )
        draw.text(
            (600, 200),
            f"NOW PLAYING",
            fill="white",
            stroke_width=2,
            stroke_fill="yellow",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 390),
                    f"Tɪᴛʟᴇ : {line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 330),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )

        draw.text(
            (600, 450),
            f"Views : {views[:23]}",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        draw.text(
            (600, 500),
            f"Duration : {duration[:23]} Mins",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        draw.text(
            (600, 550),
            f"Channel : {channel}",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
