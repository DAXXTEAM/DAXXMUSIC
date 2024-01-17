from pyrogram import Client, filters, types as t
from lexica import Client as ApiClient, AsyncClient
from pyrogram.types import InlineKeyboardButton
from math import ceil
import asyncio
from DAXXMUSIC import app



api = ApiClient()
Models = api.getModels()['models']['image']

Database = {}




async def ImageGeneration(model,prompt):
    try:
        client = AsyncClient()
        output = await client.generate(model,prompt,"")
        if output['code'] != 1:
            return 2
        elif output['code'] == 69:
            return output['code']
        task_id, request_id = output['task_id'],output['request_id']
        await asyncio.sleep(20)
        tries = 0
        image_url = None
        resp = await client.getImages(task_id,request_id)
        while True:
            if resp['code'] == 2:
                image_url = resp['img_urls']
                break
            if tries > 15:
                break
            await asyncio.sleep(5)
            resp = await client.getImages(task_id,request_id)
            tries += 1
            continue
        return image_url
    except Exception as e:
        raise Exception(f"ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ ɪᴍᴀɢᴇ: {e}")
    finally:
        await client.close()
      

def getText(message):
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

        

class EqInlineKeyboardButton(InlineKeyboardButton):
    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text

def paginate_models(page_n: int, models: list,user_id) -> list:
    modules = sorted(
        [
            EqInlineKeyboardButton(
            x['name'],
            callback_data=f"d.{x['id']}.{user_id}"
                )
                for x in models
            ]
            )

    pairs = list(zip(modules[::3], modules[1::3]))
    i = 0
    for m in pairs:
        for _ in m:
            i += 1
    if len(modules) - i == 1:
        pairs.append((modules[-1],))
    elif len(modules) - i == 2:
        pairs.append(
            (
                modules[-2],
                modules[-1],
            )
        )

    COLUMN_SIZE = 3

    max_num_pages = ceil(len(pairs) / COLUMN_SIZE)
    modulo_page = page_n % max_num_pages

    # can only have a certain amount of buttons side by side
    if len(pairs) > COLUMN_SIZE:
        pairs = pairs[
            modulo_page * COLUMN_SIZE : COLUMN_SIZE * (modulo_page + 1)
        ] + [
            (
                EqInlineKeyboardButton(
                    "◁",
                    callback_data=f"d.left.{modulo_page}.{user_id}"
                ),
                EqInlineKeyboardButton(
                    "⌯ ᴄᴀɴᴄᴇʟ ⌯",
                    callback_data=f"close_data"
                ),
                EqInlineKeyboardButton(
                    "▷",
                    callback_data=f"d.right.{modulo_page}.{user_id}"
                ),
            )
        ]
    else:
        pairs += [[EqInlineKeyboardButton("⌯ ʙᴀᴄᴋ ⌯", callback_data=f"d.-1.{user_id}")]]

    return pairs


                     



@app.on_message(filters.command(["draw","create","imagine","dream"]))
async def draw(_: app, m: t.Message):
    global Database
    prompt = getText(m)
    if prompt is None:
        return await m.reply_text("<code>ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ. ᴜsᴀɢᴇ: /draw <prompt></code>")
    user = m.from_user
    data = {'prompt':prompt,'reply_to_id':m.id}
    Database[user.id] = data
    btns = paginate_models(0,Models,user.id)
    await m.reply_text(
            text=f"**ʜᴇʟʟᴏ {m.from_user.mention}**\n\n**sᴇʟᴇᴄᴛ ʏᴏᴜʀ ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛᴏʀ ᴍᴏᴅᴇʟ**",
            reply_markup=t.InlineKeyboardMarkup(btns)
            )

@app.on_callback_query(filters.regex(pattern=r"^d.(.*)"))
async def selectModel(_:app,query:t.CallbackQuery):
    global Database
    data = query.data.split('.')
    auth_user = int(data[-1])
    if query.from_user.id != auth_user:
        return await query.answer("No.")
    if len(data) > 3:
        if data[1] == "right":
            next_page = int(data[2])
            await query.edit_message_reply_markup(
                t.InlineKeyboardMarkup(
                    paginate_models(next_page + 1,Models,auth_user)
                    )
                )
        elif data[1] == "left":
            curr_page = int(data[2])
            await query.edit_message_reply_markup(
                t.InlineKeyboardMarkup(
                    paginate_models(curr_page - 1,Models,auth_user)
                )
            )
        return
    modelId = int(data[1])
    await query.edit_message_text("**ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ, ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇ.**")
    promptData = Database.get(auth_user,None)
    if promptData is None:
        return await query.edit_message_text("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ @iam_daxx !!.")
    img_url = await ImageGeneration(modelId,promptData['prompt'])
    if img_url is None or img_url == 2 or img_url ==1:
        return await query.edit_message_text("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ @iam_dacc !!")
    elif img_url == 69:
        return await query.edit_message_text("ɴsғᴡ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ !")
    images = []
    modelName = [i['name'] for i in Models if i['id'] == modelId]
    for i in img_url:
        images.append(t.InputMediaPhoto(i))
    images[-1] = t.InputMediaPhoto(img_url[-1],caption=f"Your Prompt:\n`{promptData['prompt']}`")
    await query.message.delete()
    try:
        del Database[auth_user]
    except KeyError:
        pass
    await _.send_media_group(
        chat_id=query.message.chat.id,
        media=images,
        reply_to_message_id=promptData['reply_to_id']
        
    )





