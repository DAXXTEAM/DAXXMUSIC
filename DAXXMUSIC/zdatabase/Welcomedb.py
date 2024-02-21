from DAXXMUSIC.zdatabase import *

wlcm = dbname["welcome"]

async def add_wlcm(chat_id : int):
    return await wlcm.insert_one({"chat_id" : chat_id})
    
async def rm_wlcm(chat_id : int):   
    chat = await wlcm.find_one({"chat_id" : chat_id})
    if chat: 
        return await wlcm.delete_one({"chat_id" : chat_id})
      
