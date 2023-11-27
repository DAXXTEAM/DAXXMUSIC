"""MIT License

Copyright (c) [Year] Team DAXX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#Copyright © [LIFETIME] Team DAXX. All rights reserved




from pyrogram import Client, filters
import random
from DAXXMUSIC import app

# Constants
VALID_PREFIXES = [4, 5, 6,3]  # VISA starts with 4, MasterCard with 5, Discover with 6



def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def generate_test_card_number(prefix, length):
    card_number = [random.randint(0, 9) for _ in range(length - len(str(prefix)) - 1)]
    card_number.insert(0, str(prefix))
    card_number = ''.join(map(str, card_number))
    checksum = luhn_checksum(int(card_number) * 10)
    return card_number + str((10 - checksum) % 10)



@app.on_message(filters.command("genbin"))
def generate(client, message):
    prefix = random.choice(VALID_PREFIXES)
    length = 6  # Standard credit card length
    card_number = generate_test_card_number(prefix, length)
    message.reply_text(f"𝗬𝗢𝗨𝗥 𝗕𝗜𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗘𝗗  {card_number} ✅")
