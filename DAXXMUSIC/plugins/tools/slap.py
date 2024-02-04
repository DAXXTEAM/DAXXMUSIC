import random
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CommandHandler, ContextTypes
from DAXXMUSIC import app

# Dictionary to store different action gift links and emojis
action_info = {
    "kiss": {"links": [
        "https://telegra.ph/file/ffc013483de6f72e4626c.mp4",
        "https://telegra.ph/file/9cdac36bfa98b6f2eca19.mp4",
        "https://telegra.ph/file/3ccf3bea0ad2c33c2d5c6.mp4",
        "https://telegra.ph/file/6688a2335c252e1ddef41.mp4",
        "https://telegra.ph/file/72d5fb47c09488fe9b795.mp4",
        "https://telegra.ph/file/87d366a79bd4511fef10c.mp4",
        "https://telegra.ph/file/ce272cc604740b4e362cd.mp4"
    ], "emoji": "😘"},
    "slap": {"links": [
        "https://telegra.ph/file/10131b92e21db36414ca4.mp4",
        "https://telegra.ph/file/5386debffa02ef5e654a1.mp4",
        "https://telegra.ph/file/d9a3a2fc25ea39483e367.mp4",
        "https://telegra.ph/file/23ee740d1121f178248e1.mp4",
        "https://telegra.ph/file/928ba45c1caeabe2e339c.mp4"
    ], "emoji": "😒"},
    "hug": {"links": [
        "https://telegra.ph/file/a468af5d484eef21e16e9.mp4",
        "https://telegra.ph/file/9053a0f0c8d0410ff447d.mp4",
        "https://telegra.ph/file/80e0c3c6fc7e3f5e6f15a.mp4",
        "https://telegra.ph/file/331a7ab6f8d062654b250.mp4",
        "https://telegra.ph/file/71614a4b8011374347a51.mp4",
        "https://telegra.ph/file/ed841f3f783349c18292b.mp4"
    ], "emoji": "🤗"},
    "sleep": {"links": [
        "https://telegra.ph/file/86bbdee9fdb4f0599ebf0.mp4",
        "https://telegra.ph/file/2b1f38709806bcd85c820.mp4",
        "https://telegra.ph/file/85d5b06e887e76abd10c7.mp4",
        "https://telegra.ph/file/2c6d747e5a003030f8c2d.mp4",
        "https://telegra.ph/file/93e3061d5bdf3beac82f7.mp4",
        "https://telegra.ph/file/f7b9570807f634b96693b.mp4"
    ], "emoji": "💤"},
    "run": {"links": [
        "https://telegra.ph/file/ccb583089facc907d4e01.mp4",
        "https://telegra.ph/file/f1e716c06e605d671fa49.mp4",
        "https://telegra.ph/file/61daf6ee13005a786c951.mp4",
        "https://telegra.ph/file/32b4dbfe24520a68e063b.mp4"
    ], "emoji": "🏃"},
}

# Common function to handle actions
async def handle_action(update: Update, context: ContextTypes.DEFAULT_TYPE, action: str, action_name: str):
    sender = update.effective_user
    sender_name = f"[{sender.first_name}](tg://user?id={sender.id})"  # Clickable sender name

    if update.message.reply_to_message:
        replied_user = update.message.reply_to_message.from_user
        replied_user_name = f"[{replied_user.first_name}](tg://user?id={replied_user.id})"
        msg = f"{sender_name} sent a {action_name} to {replied_user_name}! {action_info[action]['emoji']}"
    else:
        msg = f"{sender_name} sent a {action_name} to themselves! {action_info[action]['emoji']}"

    gif_link = random.choice(action_info[action]['links'])

    # Reply with the action message using markdown
    await update.message.reply_text(text=msg, parse_mode=ParseMode.MARKDOWN)

    # Reply with the GIF below the message
    await update.message.reply_animation(animation=gif_link)

# Individual command handlers
async def kiss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_action(update, context, "kiss", "kiss")

async def slap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_action(update, context, "slap", "slap")

async def hug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_action(update, context, "hug", "hug")

async def sleep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_action(update, context, "sleep", "sleep")

async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_action(update, context, "run", "run")

# CommandHandlers
application.add_handler(CommandHandler("kiss", kiss, block=False))
application.add_handler(CommandHandler("slap", slap, block=False))
application.add_handler(CommandHandler("hug", hug, block=False))
application.add_handler(CommandHandler("sleep", sleep, block=False))
application.add_handler(CommandHandler("run", run, block=False))
