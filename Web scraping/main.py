import pandas as pd
import numpy as np
import requests
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
headerss = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-langauge': 'en-US, en;q=0.5'}
page = requests.get('https://www.daraz.com.np/laptops/?page=1&sort=order&spm=a2a0e.searchlistcategory.cate_5.4.655112fcVrPayV', headers = headerss)


# name = []
soup = BeautifulSoup(page.content,"html.parser")
title = soup.find_all('div', class_='title-wrapper--IaQ0m')


# print(name)

for titles in title:
    print(titles)



#%%
