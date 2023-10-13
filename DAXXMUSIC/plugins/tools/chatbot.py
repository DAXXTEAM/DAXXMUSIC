import import DAXX
import re
from time import sleep

import requests
from googletrans import Translator
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html

import MUSICDAXX.modules.sql.chatbot_sql as sql
from MUSICDAXX import dispatcher
from MUSICDAXX.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from MUSICDAXX.modules.helper_funcs.filters import CustomFilters
from MUSICDAXX.modules.log_channel import gloggable

tr = Translator()


@user_admin_no_reply
@gloggable
def merissarm(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"rm_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_merissa = sql.rem_merissa(chat.id)
        if is_merissa:
            is_merissa = sql.rem_merissa(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"Merissa Chatbot Disable\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "Merissa Chatbot disable by {}.".format(
                    mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@gloggable
def merissaadd(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"add_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_merissa = sql.set_merissa(chat.id)
        if is_merissa:
            is_merissa = sql.set_merissa(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"Merissa Chatbot Enable\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "Merissa Chatbot enable by {}.".format(
                    mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@gloggable
def merissa(update: Update, context: CallbackContext):
    update.effective_user
    message = update.effective_message
    msg = """**Welcome To Control Panal Of Merissa ChatBot**

**Here You Will Find Two Buttons Select AnyOne Of Them**"""
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="On", callback_data="add_chat({})"),
                InlineKeyboardButton(text="Off", callback_data="rm_chat({})"),
            ]
        ]
    )
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


def merissa_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if message.text.lower() == "merissa":
        return True
    if reply_message:
        if reply_message.from_user.id == context.bot.get_me().id:
            return True
import import html
import re
from time import sleep

import requests
from googletrans import Translator
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html

import MUSICDAXX.modules.sql.chatbot_sql as sql
from MUSICDAXX import dispatcher
from MUSICDAXX.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from MUSICDAXX.modules.helper_funcs.filters import CustomFilters
from MUSICDAXX.modules.log_channel import gloggable

tr = Translator()


@user_admin_no_reply
@gloggable
def merissarm(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"rm_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_merissa = sql.rem_merissa(chat.id)
        if is_merissa:
            is_merissa = sql.rem_merissa(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"Merissa Chatbot Disable\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "Merissa Chatbot disable by {}.".format(
                    mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@gloggable
def merissaadd(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"add_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_merissa = sql.set_merissa(chat.id)
        if is_merissa:
            is_merissa = sql.set_merissa(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"Merissa Chatbot Enable\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "Merissa Chatbot enable by {}.".format(
                    mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@gloggable
def merissa(update: Update, context: CallbackContext):
    update.effective_user
    message = update.effective_message
    msg = """**Welcome To Control Panal Of Merissa ChatBot**

**Here You Will Find Two Buttons Select AnyOne Of Them**"""
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="On", callback_data="add_chat({})"),
                InlineKeyboardButton(text="Off", callback_data="rm_chat({})"),
            ]
        ]
    )
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


def merissa_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if message.text.lower() == "merissa":
        return True
    if reply_message:
        if reply_message.from_user.id == context.bot.get_me().id:
            return True
    else:
        return False


def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    is_merissa = sql.is_merissa(chat_id)
    if not is_merissa:
        return

    if message.text and not message.document:
        if not merissa_message(context, message):
            return
        bot.send_chat_action(chat_id, action="typing")
        lang = tr.translate(message.text).src
        trtoen = (
            message.text if lang == "en" else tr.translate(message.text, dest="en").text
        ).replace(" ", "%20")
        text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
        Merissa = requests.get(
            f"https://merissachatbot.tk/api/apikey=5541274045-MERISSArC8rNQ0SK9/Merissa/Prince/message={text}"
        ).json()
        merissa = Merissa["reply"]
        msg = tr.translate(merissa, src="en", dest="hi")
        message.reply_text(msg.text)


def list_all_chats(update: Update, context: CallbackContext):
    chats = sql.get_all_merissa_chats()
    text = "<b>Merissa-Enabled Chats</b>\n"
    for chat in chats:
        try:
            x = context.bot.get_chat(int(*chat))
            name = x.title or x.first_name
            text += f"• <code>{name}</code>\n"
        except (BadRequest, Unauthorized):
            sql.rem_merissa(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")


__mod_name__ = "Chatbot 🤖"
__help__ = """
Merissa AI ChatBot is the only ai system which can detect & reply upto 200 language's

❂ `/token` : To get your Merissa Chatbot Token.
❂ `/chatbot`: To On Or Off ChatBot In Your Chat.

*Reports bugs at*: @MerissaxSupport
*Powered by* @MerissaRobot"""

CHATBOTK_HANDLER = CommandHandler("chatbot", merissa)
ADD_CHAT_HANDLER = CallbackQueryHandler(merissaadd, pattern=r"add_chat")
RM_CHAT_HANDLER = CallbackQueryHandler(merissarm, pattern=r"rm_chat")
CHATBOT_HANDLER = MessageHandler(
    Filters.text
    & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!") & ~Filters.regex(r"^\/")),
    chatbot,
)
LIST_ALL_CHATS_HANDLER = CommandHandler(
    "allchats", list_all_chats, filters=CustomFilters.dev_filter
)

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(CHATBOTK_HANDLER)
dispatcher.add_handler(RM_CHAT_HANDLER)
dispatcher.add_handler(LIST_ALL_CHATS_HANDLER)
dispatcher.add_handler(CHATBOT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
    LIST_ALL_CHATS_HANDLER,
    CHATBOT_HANDLER,
]    else:
        return False


def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    is_merissa = sql.is_merissa(chat_id)
    if not is_merissa:
        return

    if message.text and not message.document:
        if not merissa_message(context, message):
            return
        bot.send_chat_action(chat_id, action="typing")
        lang = tr.translate(message.text).src
        trtoen = (
            message.text if lang == "en" else tr.translate(message.text, dest="en").text
        ).replace(" ", "%20")
        text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
        Merissa = requests.get(
            f"https://merissachatbot.tk/api/apikey=5541274045-MERISSArC8rNQ0SK9/Merissa/Prince/message={text}"
        ).json()
        merissa = Merissa["reply"]
        msg = tr.translate(merissa, src="en", dest="hi")
  message.reply_text(msg.text)


def list_all_chats(update: Update, context: CallbackContext):
    chats = sql.get_all_merissa_chats()
    text = "<b>Merissa-Enabled Chats</b>\n"
    for chat in chats:
        try:
            x = context.bot.get_chat(int(*chat))
            name = x.title or x.first_name
            text += f"• <code>{name}</code>\n"
        except (BadRequest, Unauthorized):
            sql.rem_merissa(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")


__mod_name__ = "Chatbot 🤖"
__help__ = """
Merissa AI ChatBot is the only ai system which can detect & reply upto 200 language's

❂ `/token` : To get your Merissa Chatbot Token.
❂ `/chatbot`: To On Or Off ChatBot In Your Chat.

*Reports bugs at*: @MerissaxSupport
