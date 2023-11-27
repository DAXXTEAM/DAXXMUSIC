from pyrogram import Client, filters
import random
from DAXXMUSIC import app

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10 == 0

def generate_credit_card_number():
    card_num = [random.randint(0, 9) for _ in range(6)] 
    
    for i in range(10): 
        card_num[0] = i  
        if luhn_check(int(''.join(map(str, card_num)))):
            return '4' + ''.join(map(str, card_num)) 
    return generate_credit_card_number() 
@app.on_message(filters.command("genbin"))
def send_credit_card_number(client, message):
    card_number = generate_credit_card_number()
    message.reply(f"Generated A Credit Card Number: {card_number}", quote=True)
