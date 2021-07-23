import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/"
r = requests.get(url)
yahoo_html = r.text

soup = BeautifulSoup(yahoo_html, 'html_parser')
print(soup.prettify)

print(soup.title)
print(soup.title.name)
print(soup.title.string)

for link in soup.find_all("a", class_="sc-jwKygS"):
  print(link.get_text())
  print(link.get('href'))

