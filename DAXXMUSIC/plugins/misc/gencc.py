from pyrogram import Client, filters
from DAXXMUSIC import app
from faker import Faker
fake = Faker()


# Function to generate a list of test credit card numbers
def generate_test_credit_cards(quantity=10):
    card_numbers = []
    for _ in range(quantity):
        card_details = fake.credit_card_full().split("\n")  # Includes card number, expiry date, and CVV
        card_numbers.append(card_details)
    return card_numbers
    
# Command handler to provide credit card numbers
@app.on_message(filters.command("gencc"))
def send_cards(client, message):
    quantity = 10  # Adjust this value to change the number of cards generated
    test_cards = generate_test_credit_cards(quantity)
    response = "Generated Credit Card Numbers:\n"
    for card in test_cards:
        response += "\n".join(card) + "\n---\n"
    message.reply_text(response)
