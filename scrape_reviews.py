from bs4 import BeautifulSoup
import requests

url = "https://apps.apple.com/in/app/instagram/id389801252"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
