#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


get_ipython().system('pip install beautifulsoup4')


# In[ ]:





# In[3]:


from selenium import webdriver
import time
import pandas as pd
import os
import datetime


# In[4]:


USER = "test_*user"
PASS = "test_pw"


# In[8]:


# GoogleChromeを起動
browser = webdriver.Chrome(executable_path = 'C:\\Users\YataniMakio.MYCOMPUTER\\anaconda3\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe')
browser.implicitly_wait(3)


# In[10]:


#ログインページするサイトへアクセス
url_login = "https://kino-code.work/"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました")


# In[11]:


# テキストボックス入力
elem = browser.find_element_by_id('swpm_user_name')
elem.clear()
elem.send_keys(USER)
elem = browser.find_element_by_id('swpm_password')
elem.clear()
elem.send_keys(PASS)
print("フォームを送信")


# In[ ]:


# 入力したデータをクリック
browser_from = browser.find_element_by_name('swpm-login')
time.sleep(3)
browser_from.click()
print("情報を入力してログインボタンを押しました")


# In[ ]:


# ウェブサイトへアクセス
url = "https://kino-code.com/member-only/"
time.sleep(1)
browser.get(url)
print(url, ":アクセス完了")


# In[ ]:


# ダウンロードボタンをクリック
# 検証→クリック→右クリック→Copy Full Xpath
frm = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/main/article/div/p[2]/button')
time.sleep(1)
frm.click()
print('ダウンロードボタンをクリック')
