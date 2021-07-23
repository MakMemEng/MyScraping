from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd

chrome_path = 'C:\\Users\YataniMakio.MYCOMPUTER\\anaconda3\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

url = 'https://www.google.com/imghp?hl=ja'
driver.get(url)

sleep(3)

query = 'プログラミング'
search_box = driver.find_element_by_name('q').send_keys(query, Keys.ENTER)

sleep(3)

height = 1000
while height < 3000:
    driver.execute_script("window.scrollTo(0, {});".format(height))
    height += 100
    print(height)

    sleep(1)

# 画像の要素を選択
elements = driver.find_elements_by_class_name('rg_i Q4LuWd')

d_list = []
# 要素からURLを取得
for i, element in enumerate(elements, start=1):
    name = f'{query}_{i}'
    raw_url = element.find_element_by_class_name('VFACy kGQAp sMi44c lNHeqe WGvvNb').get_attribute('href')
    google_image_url = element.find_element_by_tag_name('img').get_attribute('src')
    title = element.find_element_by_tag_name('img').get_attribute('src')

    d = {
        'filename': name,
        'raw_url': raw_url,
        'google_image_url': google_image_url,
        'title': title
    }

    d_list.append(d)

    sleep(2)

df = pd.DataFrame(d_list)
df.to_csv('image_urls_20200223.csv')

driver.quit()