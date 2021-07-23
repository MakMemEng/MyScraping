import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/"
r = requests.get(url)
yahoo_html = r.text

soup = BeautifulSoup(yahoo_html, 'html.parser')
soup