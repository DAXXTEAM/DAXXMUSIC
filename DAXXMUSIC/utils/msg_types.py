import re
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import BOT_USERNAME
from DAXXMUSIC.mongo.notesdb import isNoteExist

BTN_URL_REGEX = re.compile(
    r"(\[([^\[]+?)\]\(buttonurl:(?:/{0,2})(.+?)(:same)?\))"
)

def button_markdown_parser(text):
    
    markdown_note = None
    markdown_note = text
    text_data = ""
    buttons = []
    if markdown_note is None:
        return text_data, buttons
    #
    if markdown_note.startswith('/'):
        args = markdown_note.split(None, 2)
        # use python's maxsplit to separate cmd and args
        markdown_note = args[2]
    prev = 0
    for match in BTN_URL_REGEX.finditer(markdown_note):
        # Check if btnurl is escaped
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and markdown_note[to_check] == "\\":
            n_escapes += 1
            to_check -= 1

        # if even, not escaped -> create button
        if n_escapes % 2 == 0:
            # create a thruple with button label, url, and newline status
            if bool(match.group(4)) and buttons:
                buttons[-1].append(InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(3)
                ))
            else:
                buttons.append([InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(3)
                )])
            text_data += markdown_note[prev:match.start(1)]
            prev = match.end(1)
        # if odd, escaped -> move along
        else:
            text_data += markdown_note[prev:to_check]
            prev = match.start(1) - 1
    else:
        text_data += markdown_note[prev:]

    return text_data, buttons
