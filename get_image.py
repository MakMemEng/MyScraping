# ライブラリのインポート
import os
from time import sleep
import codecs
import random

import pandas as pd
import requests

IMAGE_DIR = './images/'

# CSVの読み込み
with codecs.open("image_yahoo_urls_20200223.csv", "r", "shift-jis", "ignore") as file:
    df = pd.read_table(file, delimiter=",")
    print(df)

if os.path.isdir(IMAGE_DIR):
    print('既にあります！')
else:
    os.makedirs(IMAGE_DIR)


# 画像の保存
for file_name, yahoo_image_url in zip(df.filename[:5], df.yahoo_image_url[:5]):
    image = requests.get(yahoo_image_url)
    with open(IMAGE_DIR + file_name + '.jpg', 'wb', ) as f:
        f.write(image.content)

    sleep(
        random.randint(1, 10, 5, 4, 2)
    )

