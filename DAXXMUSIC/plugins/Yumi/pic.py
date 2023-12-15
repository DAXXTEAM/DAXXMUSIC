"""** MIT License

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
SOFTWARE. **"""


from pyrogram import Client, filters
import requests
from pyrogram.types import Message
from io import BytesIO
from DAXXMUSIC import app

# Fill these out with your credentials


def get_random_picture():
    response = requests.get('https://source.unsplash.com/random')
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        return None  # If something went wrong


# Command handler to respond to /pic commands
@app.on_message(filters.command("randompic"))
def pic(client, message):
    random_pic = get_random_picture()
    if random_pic:
        message.reply_photo(random_pic)
    else:
        message.reply("Sorry, I couldn't get a random picture at the moment. 😔")



#____________________________

@app.on_message(filters.command("pic"))
def pic_command(client, message: Message):
    # Extract the name from the command
    try:
        name = message.command[1]
    except IndexError:
        client.send_message(message.chat.id, "Please provide a name after the /pic command.")
        return

    # Build the Unsplash URL with the provided name
    unsplash_url = f"https://source.unsplash.com/500x500/?{name}"

    # Send the image as a photo
    try:
        response = requests.get(unsplash_url)
        if response.status_code == 200:
            client.send_photo(message.chat.id, photo=unsplash_url, caption=f"Here's a picture related to {name}.")
        else:
            client.send_message(message.chat.id, "Failed to fetch image.")
    except requests.RequestException as e:
        client.send_message(message.chat.id, f"An error occurred: {str(e)}")        
