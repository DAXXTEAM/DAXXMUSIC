from pyrogram import Client, filters
import requests
from DAXXMUSIC import app

API_URL = "https://graphql.anilist.co"

@app.on_message(filters.command(["Anime"], prefixes="/"))
def get_anime_info(_, message):
    # Get the anime name from the command
    anime_name = message.text.split("/Anime")[1].strip()

    # Make a request to the AniList GraphQL API
    query = """
    query ($anime_name: String) {
      Media(search: $anime_name, type: ANIME) {
        title {
          romaji
          english
          native
        }
        description
        episodes
        coverImage {
          large
        }
      }
    }
    """

    variables = {"anime_name": anime_name}
    response = requests.post(API_URL, json={"query": query, "variables": variables})

    if response.status_code == 200:
        # Extract relevant information from the response
        data = response.json()["data"]["Media"]
        title = data["title"]["romaji"] or data["title"]["english"] or data["title"]["native"]
        description = data["description"]
        episodes = data["episodes"]
        image_url = data["coverImage"]["large"]

        # Create a message with anime information and the cover image
        anime_info = f"Title: {title}\nEpisodes: {episodes}\nDescription: {description}"
        app.send_photo(chat_id=message.chat.id, photo=image_url, caption=anime_info)
    else:
        anime_info = "Anime not found. Please check the name and try again."
        message.reply_text(anime_info)
