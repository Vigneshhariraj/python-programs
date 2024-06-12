import requests
from bs4 import BeautifulSoup as bs

# URL of the GitHub profile
github_profile = "https://github.com/Vigneshhariraj"

# Send a GET request to the profile page
req = requests.get(github_profile)

# Parse the content with BeautifulSoup
scraper = bs(req.content, "html.parser")

# Find the profile picture URL
# GitHub profile pictures often have a specific class "avatar-user"
profile_picture = scraper.find("img", {"class": "avatar-user"})["src"]

print(profile_picture)
