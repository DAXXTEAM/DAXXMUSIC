import json
import os
import requests
from pyrogram import filters
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import Message
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
from DAXXMUSIC import app


@app.on_message(filters.command(["exampur"]))
async def account_login(_, Message):
    global cancel
    cancel = False
    rwa_url = "https://auth.exampurcache.xyz/auth/login"
    
    hdr = {
           "appauthtoken": "no_token",
           "User-Agent": "Dart/2.15(dart:io)",
           "content-type": "application/json; charset=UTF-8",       
           "Accept-Encoding": "gzip",
           "content-length": "94",
           "host": "auth.exampurcache.xyz" 
          }
    info={"phone_ext": "91", "phone": "", "email": "", "password": ""}
    input1 = await app.ask(message.chat.id, text="Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    scraper = cloudscraper.create_scraper()
    res = scraper.post(rwa_url, data=info).content
    output = json.loads(res)
    token = output["data"]["authToken"]
    hdr1 = {
            "appauthtoken": token,
            "User-Agent": "Dart/2.15(dart:io)",
            "Accept-Encoding": "gzip",
            "host": "auth.exampurcache.xyz"
            }
    lol = await message.reply_text("**login Successful**")

    res1 = requests.get("https://auth.exampurcache.xyz/mycourses", headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa = f" ```{data['_id']}```      - **{data['title']}**\n\n"
        # aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await lol.edit_text(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text

    scraper = cloudscraper.create_scraper()
    html = scraper.get("https://auth.exampurcache.xyz/course_subject/" + raw_text2,headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    vj = ""
    for data in subjID:
       tids = (data["_id"])
       b = (data["title"])
       idid = f"{tids}&"
       if len(f"{vj}{idid}") > 4096:
          vj = ""
       vj += idid
    raw=vj
    await message.reply_text(raw)

    input4 = await app.ask(message.chat.id, text=f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{raw}```")
    raw_text4 = input4.text
    try:
        xv = raw_text4.split('&')
        for y in range(0,len(xv)):
            t =xv[y]

            res4 = requests.get("https://auth.exampurcache.xyz/course_material/chapter/"+t+"/" + raw_text2,headers=hdr1)
            b_data2 = res4.json()['data']
            
            vj = ""
            for i in range(0, len(b_data2)):
               tids = (b_data2[i])
               idid = f"{tids}"
               if len(f"{vj}{idid}") > 4096:
                  vj = ""
               encoded_URL = urllib.parse.quote(idid, safe="")
               chapter = encoded_URL.replace("%28", "(").replace("%29", ")").replace("%26", "&")
               vj += chapter
               res5 = requests.get("https://auth.exampurcache.xyz/course_material/material/"+t+"/"+raw_text2+"/"+chapter,headers=hdr1)
               b_data3 = res5.json()['data']
               vk = ""
               for data in b_data3:
                  tids = (data["video_link"])
                  b = (data["title"])
                  cc = (f"{b}:{tids}\n")

                  vk += cc

               mm = "Exampur"
               with open(f'{mm}.txt', 'a') as f:
                   f.write(f"{cc}")
               await message.reply_document(f"{mm}.txt")
    except Exception as e:
        await message.reply_text(str(e))
    await message.reply_text("Done")
