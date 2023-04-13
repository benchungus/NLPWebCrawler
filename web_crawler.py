from bs4 import BeautifulSoup
import requests

# Replace the URL with the actual URL of the category page you want to scrape
url = "https://despicableme.fandom.com/wiki/Category:Characters"

# Send a request to the URL and get the HTML response
response = requests.get(url)

# Parse the HTML response using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the category page member links
member_links = soup.find_all("a", class_="category-page__member-link")

# Print the member links
for link in member_links:
    print(link["href"])