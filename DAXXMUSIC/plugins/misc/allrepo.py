"""
                                                                        
────────────────────────────────────────────────────────────────────────
─████████████────██████████████──████████──████████──████████──████████─
─██░░░░░░░░████──██░░░░░░░░░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─██░░████░░░░██──██░░██████░░██──████░░██──██░░████──████░░██──██░░████─
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░░░░░░░░░██──────██░░░░░░██──────────██░░░░░░██─────
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░████░░░░██──██░░██──██░░██──████░░██──██░░████──████░░██──██░░████─
─██░░░░░░░░████──██░░██──██░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─████████████────██████──██████──████████──████████──████████──████████─
──────────────────────────────────────────────────────────────────────── ** 

""""



from pyrogram import Client, filters
import requests
from DAXXMUSIC import app


@app.on_message(filters.command("allrepo"))
async def all_repo_command(client, message):
    try:
        # Check if there is a GitHub username after the /allrepo command
        if len(message.command) > 1:
            github_username = message.command[1]

            # Fetch all repositories of the GitHub user
            repo_links = get_all_repositories(github_username)

            # Send the repository links as a reply
            await message.reply_text(repo_links)
        else:
            await message.reply_text("Please enter a GitHub username after the /allrepo command.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

def get_all_repositories(github_username):
    # Set up the GitHub API URL for user repositories
    github_api_url = f"https://api.github.com/users/{github_username}/repos"

    # Perform the request to the GitHub API
    response = requests.get(github_api_url)
    data = response.json()

    # Extract relevant information from the response
    repo_links = "\n".join([f"{repo['full_name']}: {repo['html_url']}" for repo in data])

    return repo_links
