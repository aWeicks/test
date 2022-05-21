# retriver.py - gets html content from target page and outputs multiple usable data formats

import requests

from bs4 import BeautifulSoup




page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')