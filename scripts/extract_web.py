import requests
from bs4 import BeautifulSoup

def scrape_web():
    html = requests.get("https://example.com").text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.text
    print("Website Title:", title)
    return title

if __name__ == "__main__":
    scrape_web()
