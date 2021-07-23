import requests

url = "https://news.yahoo.co.jp/"
r = requests.get(url)
r.text
