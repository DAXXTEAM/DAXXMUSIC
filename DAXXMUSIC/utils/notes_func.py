from enum import Enum, auto
from pyrogram.types import Message
import html
import re
from pyrogram.types import InlineKeyboardMarkup
from DAXXMUSIC import app
from DAXXMUSIC.mongo.notesdb import GetNote
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from DAXXMUSIC.utils.msg_types import button_markdown_parser

class NoteTypeMap(Enum):
    text = auto()
    sticker = auto()
    animation= auto()
    document = auto()
    photo = auto()
    audio = auto()
    voice = auto()
    video = auto()
    video_note = auto()

def GetNoteMessage(message):
    data_type = None
    content = None
    text = str()

    raw_text = message.text or message.caption
    args = raw_text.split(None, 2)
    
    if len(args) >= 3 and not message.reply_to_message:
        text = message.text.markdown[len(message.command[0]) + len(message.command[1]) + 2 :]
        data_type = NoteTypeMap.text.value

    if (
        message.reply_to_message
        and message.reply_to_message.text
    ):
        if len(args) >= 2:
            text = message.reply_to_message.text.markdown
            data_type = NoteTypeMap.text.value
            
    elif (
        message.reply_to_message
        and message.reply_to_message.sticker
    ):
        content = message.reply_to_message.sticker.file_id
        data_type = NoteTypeMap.sticker.value

    elif (
        message.reply_to_message
        and message.reply_to_message.animation
    ):
        content = message.reply_to_message.animation.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = NoteTypeMap.animation.value

    elif (
        message.reply_to_message
        and message.reply_to_message.document
    ):
        content = message.reply_to_message.document.file_id
        if message.reply_to_message.caption: 
            text = message.reply_to_message.caption.markdown 
        data_type = NoteTypeMap.document.value

    elif (
        message.reply_to_message
        and message.reply_to_message.photo
    ):
        content = message.reply_to_message.photo.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = NoteTypeMap.photo.value

    elif (
        message.reply_to_message
        and message.reply_to_message.audio
    ):
        content = message.reply_to_message.audio.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type = NoteTypeMap.audio.value

    elif (
        message.reply_to_message
        and message.reply_to_message.voice
    ):
        content = message.reply_to_message.voice.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = NoteTypeMap.voice.value

    elif (
        message.reply_to_message
        and message.reply_to_message.video
    ):
        content = message.reply_to_message.video.file_id 
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type = NoteTypeMap.video.value

    elif (
        message.reply_to_message
        and message.reply_to_message.video_note
    ):
        content = message.reply_to_message.video_note.file_id
        data_type = NoteTypeMap.video_note.value
    
    return (
        content,
        text,
        data_type
    )
  
def NoteFillings(message, message_text):
  if not message == None:
    user_id = message.from_user.id 
    first_name = message.from_user.first_name 
    last_name = message.from_user.last_name
    if last_name == None:
      last_name = ''
    full_name = f'{first_name} {last_name}'
    username = message.from_user.username
    mention = message.from_user.mention 
    chat_title = message.chat.title
    
    try:
      FillingText = message_text.format(
        id=user_id,
        first=first_name,
        fullname=full_name,
        username=username,
        mention=mention,
        chatname=chat_title
        ) 
    except KeyError:
      FillingText = message_text

  else:
    FillingText = message_text
  
  return FillingText


async def SendNoteMessage(message: Message, note_name: str, from_chat_id: int):
    user_id = message.from_user.id
    if from_chat_id is not None:
            message_id = message.id
            chat_id = message.from_user.id
            content, text, data_type = await GetNote(from_chat_id, note_name)
            text = (
                f"**{note_name}:**\n\n"
                f"{text}"
            ) 

    else:
        message_id = message.id
        if message.reply_to_message:
            message_id = message.reply_to_message.id
        chat_id = message.chat.id 
        content, text, data_type = await GetNote(chat_id, note_name)
    
    
    text, buttons = button_markdown_parser(text)
    preview, text = preview_text_replace(text)

    text = NoteFillings(message, text)

    text = html.escape(text)
    if (
        not text
        or re.search(r"^\s*$", text)
    ):
        text = note_name

    reply_markup = None
    if len(buttons) > 0:
        reply_markup = InlineKeyboardMarkup(buttons)
    else:
        reply_markup = None

    if (
        data_type == 1
    ):
        await app.send_message(
            chat_id=chat_id,
            text=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup,
            disable_web_page_preview=preview
        )
    
    elif (
        data_type == 2
    ):
        await app.send_sticker(
            chat_id=chat_id,
            sticker=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 3
    ):
        await app.send_animation(
            chat_id=chat_id,
            animation=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        data_type == 4
    ):
        
        await app.send_document(
            chat_id=chat_id,
            document=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        data_type == 5
    ):
        await app.send_photo(
            chat_id=chat_id,
            photo=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )  
    
    elif (
        data_type == 6
    ):
        await app.send_audio(
            chat_id=chat_id,
            audio=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    elif (
        data_type == 7
    ):
        await app.send_voice(
            chat_id=chat_id,
            voice=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 8
    ):
        await app.send_video(
            chat_id=chat_id,
            video=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 9
    ):
        await app.send_video_note(
            chat_id=chat_id,
            video_note=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    return 

async def exceNoteMessageSender(message, note_name, from_chat_id=None):
    try:
        await SendNoteMessage(message, note_name, from_chat_id)
    except Exception as e:
        await message.reply(
            (
                "The notedata was incorrect, please update it. The buttons are most likely to be broken. If you are sure you aren't doing anything wrong and this was unexpected - please report it in my support chat.\n"
                f"**Error:** `{e}`"
            ),
            quote=True
        )

async def isUserAdmin(message: Message, pm_mode: bool = False, user_id: int = None, chat_id: int = None, silent: bool = False) -> bool:
    if user_id is None:
        user_id = message.from_user.id

    if chat_id is None:
        chat_id = message.chat.id 

    if not pm_mode: 
        if message.chat.type == 'private':
            return True  

    GetData = await app.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    
    if GetData.privileges:
        return True
    else:
        if not silent:
            await message.reply(
                "Only admins can execute this command!"
            )
        return False
    
    
async def privateNote_and_admin_checker(message, text: str):
    privateNote = True
    if '{noprivate}' in text:
        privateNote = False 
    elif '{private}' in text:
        privateNote = True 
    else:
        privateNote = None

    allow = True
    if '{admin}' in text:
        if not await isUserAdmin(message, silent=True):
            allow = False 
        else:
            allow = True 
    
    return (
        privateNote,
        allow
    )

def preview_text_replace(text):
        if '{preview}' in text:
            text = text.replace('{preview}', '')
            preview =  False
        else:
            preview = True
        
        if '{admin}' in text:
            text = text.replace('{admin}', '')
        
        if '{private}' in text:
            text = text.replace('{private}', '')
        elif '{noprivate}' in text:
            text = text.replace('{noprivate}', '')
        
        return (
            preview, text
        )
