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


from pyrogram import Client, filters
from faker import Faker
from DAXXMUSIC import app

# Create a Faker instance
fake = Faker()




# Generate person info command handler
@app.on_message(filters.command("data"))
def generate_person(_, message):
    name = fake.name()
    email = fake.email()
    address = fake.address()
    phone_number = fake.phone_number()
    job = fake.job()
    ssn = fake.ssn()

    response = (
        f"𝗡𝗔𝗠𝗘: {name}\n"
        f"𝗘𝗠𝗔𝗜𝗟: {email}\n"
        f"𝗔𝗗𝗗𝗥𝗘𝗦𝗦: {address}\n"
        f"𝗣𝗛𝗢𝗡𝗘: {phone_number}\n"
        f"𝗝𝗢𝗕: {job}\n"
        f"𝗦𝗦𝗡: {ssn}"
    )
    
    message.reply_text(response)

# Run the bot