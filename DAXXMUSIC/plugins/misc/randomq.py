from pyrogram import Client, filters
from DAXXMUSIC import app

message_counts = {}


questions = ["What is your favorite book?", "What's the most interesting place you've ever visited?", "What hobby would you get into if time and money weren’t an issue?", "If you could live anywhere, where would it be?", "What is your favorite type of music and why?", "If you could have any superpower, what would it be and how would you use it?", "What is the most memorable vacation you have ever taken and why?", "If you could have dinner with any historical figure, who would it be and why?", "What is your favorite book or movie and why does it resonate with you?", "If you could live in any fictional world, which one would you choose and why?", "What is the most adventurous thing you have ever done in your life?", "If you could change one thing about the world, what would it be and why?","What is your favorite quote and why does it inspire you?", "If you could learn any new skill instantly, what would it be and why?", "What is your favorite childhood memory and why does it stand out to you?", "If you could have a conversation with any animal, which one would you choose and what would you ask it?", "What is the best piece of advice you have ever received and how has it impacted your life?", "If you could travel back in time to any era, which one would you choose and why?", "What is your dream job and why does it appeal to you?", "If you could have a dinner party with any three people, dead or alive, who would you invite and why?", "What is the most challenging thing you have ever accomplished and how did it change you?", "If you could visit any country in the world, where would you go and why?", "What is your favorite hobby or activity and why do you enjoy it?", "If you could have a conversation with your future self, what advice would you ask for?"]

@app.on_message(filters.group)
async def count_messages(client, message):
    chat_id = message.chat.id
    
    
    if chat_id in message_counts:
        message_counts[chat_id] += 1
    else:
        message_counts[chat_id] = 1

    
    if message_counts[chat_id] >= 20:
        
        message_counts[chat_id] = 0
        
       
        question = questions.pop(0)  
        await app.send_message(chat_id, question)

        
        questions.append(question)
