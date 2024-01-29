from pyrogram import Client, filters
from pymongo import MongoClient
from DAXXMUSIC import app
from config import MONGO_DB_URI
import config

mongo_uri = config.MONGO_DB_URI


mongo_client = MongoClient(mongo_uri)
db = mongo_client["your_database_name"]
top_members_collection = db["top_members"]

user_data = {}




@app.on_message(filters.command("ranking"))
def top_members(_, message):
    top_members = top_members_collection.find().sort("total_messages", -1).limit(10)
    
    response = "Top 10 Members by Message Count:\n"
    for idx, member in enumerate(top_members, start=1):
        user_id = member["_id"]
        total_messages = member["total_messages"]
        user_info = f"{idx}. User ID: {user_id}, Total Messages: {total_messages}\n"
        response += user_info

    message.reply_text(response)


@app.on_message()
def handle_messages(_, message):
    user_id = message.from_user.id

    
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1

    
    top_members_collection.update_one({"_id": user_id}, {"$inc": {"total_messages": 1}}, upsert=True)
