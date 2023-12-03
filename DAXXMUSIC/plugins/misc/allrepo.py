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
────────────────────────────────────────────────────────────────────────

"""


@app.on_message(filters.command("allrepo"))
async def all_repo_command(client, message):
    try:
        # Check if there is a GitHub username after the /allrepo command
        if len(message.command) > 1:
            github_username = message.command[1]

            # Fetch information about all repositories of the GitHub user
            repo_info = get_all_repository_info(github_username)

            # Send the repository information as a reply
            await message.reply_text(repo_info)
        else:
            await message.reply_text("Please enter a GitHub username after the /allrepo command.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

def get_all_repository_info(github_username):
    # Set up the GitHub API URL for user repositories
    github_api_url = f"https://api.github.com/users/{github_username}/repos"

    # Perform the request to the GitHub API
    response = requests.get(github_api_url)
    data = response.json()

    # Extract relevant information from the response
    repo_info = "\n\n".join([
        f"Repository: {repo['full_name']}\n"
        f"Description: {repo['description']}\n"
        f"Stars: {repo['stargazers_count']}\n"
        f"Forks: {repo['forks_count']}\n"
        f"URL: {repo['html_url']}"
        for repo in data
    ])

    return repo_info





########### COPY PASTE KRLO BUT CREDIT DEKE JANA BHOSDI WALO
