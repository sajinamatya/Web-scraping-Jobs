# import pandas as pd
# import numpy as np
import requests

from bs4 import BeautifulSoup
# from time import sleep
# from random import randint

headerss = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-langauge': 'en-US, en;q=0.5'}
page = requests.get('https://merojob.com/category/it-telecommunication/')
soup = BeautifulSoup(page.content,"lxml")
title = soup.find_all('div', class_='card-body')
titlelist =[]
for each in title:
    for each1 in each.find_all('h1'):
        for each2 in each1.find_all('a'):
            titlelist.append(each2.text)


cleaned_title = [job.strip() for job in titlelist]
print(cleaned_title)






#%%

#%%
