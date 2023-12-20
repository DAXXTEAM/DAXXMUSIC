"""**
MIT License

Copyright (c) [All] [DAXX TEAM]

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
LIABILITY, WHETHER IN AN ACTION**
"""





from pyrogram import Client, filters
import git
import shutil
import os
from DAXXMUSIC import app



@app.on_message(filters.command(["downloadrepo"]))
def download_repo(_, message):
    if len(message.command) != 2:
        message.reply_text("Please provide the GitHub repository URL after the command. Example: /downloadrepo Repo Url ")
        return

    repo_url = message.command[1]
    zip_path = download_and_zip_repo(repo_url)

    if zip_path:
        with open(zip_path, "rb") as zip_file:
            message.reply_document(zip_file)
        os.remove(zip_path)
    else:
        message.reply_text("Unable to download the specified GitHub repository.")


def download_and_zip_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"{repo_name}"
        
        # Clone the repository
        repo = git.Repo.clone_from(repo_url, repo_path)
        
        # Create a zip file of the repository
        shutil.make_archive(repo_path, 'zip', repo_path)

        return f"{repo_path}.zip"
    except Exception as e:
        print(f"Error downloading and zipping GitHub repository: {e}")
        return None
    finally:
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
