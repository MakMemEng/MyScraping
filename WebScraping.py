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


# In[21]:


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


# In[ ]:





# In[12]:


from bs4 import BeautifulSoup
import urllib.request as req


# In[13]:


html="""
<html>
    <head>
        <meta charset="utf-8">
        <title>キノコード</title>
    </head>
    <body>
        <h1>こんにちは</h1>
    </body>
</html>
"""


# In[14]:


html


# In[15]:


parse_html = BeautifulSoup(html, 'html.parser')


# In[16]:


print(parse_html)


# In[17]:


print(parse_html.prettify())


# In[38]:


url = "https://kino-code.work/python-super-basic-course/"
response = req.urlopen(url)


# In[39]:


parse_html = BeautifulSoup(response, 'html.parser')


# In[40]:


parse_html


# In[41]:


print(parse_html.title)


# In[42]:


print(parse_html.title.string)


# In[43]:


print(parse_html.find_all('a'))


# In[44]:


title_lists=parse_html.find_all('a')


# In[45]:


title_lists[1:10]


# In[46]:


title_lists[10].string


# In[47]:


title_lists[10].attrs['href']


# In[48]:


title_list=[]
url_list=[]

for i in title_lists:
    title_list.append(i.string)
    url_list.append(i.attrs['href'])


# In[49]:


title_list


# In[50]:


url_list


# In[51]:


df_title_url = pd.DataFrame({'Title':title_list, 'URL':url_list})


# In[52]:


df_title_url


# In[53]:


df_notnull = df_title_url.dropna(how='any')


# In[54]:


df_notnull


# In[55]:


# 特定の文字列が含まれているか判定
df_notnull['Title'].str.contains('Python超入門コース')


# In[56]:


df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]


# In[57]:


df_contain_python = df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]


# In[58]:


df_contain_python


# In[59]:


df_contain_python.to_csv('output.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




