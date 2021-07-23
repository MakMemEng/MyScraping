import requests
from bs4 import BeautifulSoup
import time

url = "https://news.yahoo.co.jp/"

soup = BeautifulSoup(yahoo_html, 'html_parser')

def print_topics(soup):
  for link in soup.find_all("a", class_="sc-jwKygS"):
    print(link.get_text())
    print(link.get('href'))

urls = {
  '経済' : 'https://news.yahoo.co.jp/categories/business',
  'IT' : 'https://news.yahoo.co.jp/categories/it',
  '科学' : 'https://news.yahoo.co.jp/categories/science'
}

print_topics(soup)

def get_content(url):
  r = requests.get(url)
  yahoo_html = r.text 
  soup = BeautifulSoup(yahoo_html, 'html.parser')
  return soup

get_content(urls['経済'])

for name, url in urls.items():
  soup = get_content(url)
  print("【{}】".format(name))
  print_topics(soup)
  time.sleep(5)