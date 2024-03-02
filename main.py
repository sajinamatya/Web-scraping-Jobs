<<<<<<< HEAD
import pandas as pd
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


titlelist = []
company=[]
views=[]

# Function for Extracting the data from the website using bs4
def data_extract():
    for page in range(1, 6):

        headerss = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-langauge': 'en-US, en;q=0.5'}
        request = requests.get('https://merojob.com/category/it-telecommunication/?page='+str(page))
        soup = BeautifulSoup(request.content,"lxml")

        title = soup.find_all('div', class_='card-body')

        for each in title:
            [titlelist.append(each2.text) for each1 in each.find_all('h1') for each2 in each1.find_all('a')]


            for company1 in each.find_all('h3'):
                a = company1.find('a')
                if a:
                   company.append(a.text)
                else:
                    span = company1.find('span')
                    if span:
                        company.append(span.text)

        footer_card = soup.find_all('div',class_="card-footer py-2")
        [views.append(view1.text) for view in footer_card for view1 in view.find_all('span',class_="text-primary mr-2")]

           # sleep(randint(2,7))

    footer_card = soup.find_all('div',class_="card-footer py-2")
    
    for view in footer_card:
        for view1 in view.find_all('span',class_="text-primary mr-2"):
            views.append(view1.text)


data_extract()


#Function for transforming and cleaning the extracted data
def data_transform():

    cleaned_title = [job.strip() for job in titlelist]
    cleaned_company =[companys.strip() for companys in company]
    cleaned_view = [view.replace('Views: ','').strip() for view in views]

     sleep(randint(2,10))
    
cleaned_title = [job.strip() for job in titlelist]

cleaned_company =[companys.strip() for companys in company]

cleaned_view = [view.replace('Views: ','').strip() for view in views]

    return cleaned_title, cleaned_company, cleaned_view

dict = {'job title': data_transform()[0] ,'Company':data_transform()[1],'View':data_transform()[2]}


# Function for loading the data in excel format
def data_load():
    df = pd.DataFrame(dict)
    df.to_excel('job.xlsx')
    return df
print(data_load())



df = pd.DataFrame(dict)

df.to_excel('job.xlsx')


print(df)








=======
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

# List
titlelist = []
company=[]
views=[]

# Function for Extracting the data from the website using bs4
def data_extract():
    for page in range(1, 6):

        headerss = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-langauge': 'en-US, en;q=0.5'}
        request = requests.get('https://merojob.com/category/it-telecommunication/?page='+str(page))
        soup = BeautifulSoup(request.content,"lxml")

        title = soup.find_all('div', class_='card-body')

        for each in title:
            [titlelist.append(each2.text) for each1 in each.find_all('h1') for each2 in each1.find_all('a')]


            for company1 in each.find_all('h3'):
                a = company1.find('a')
                if a:
                   company.append(a.text)
                else:
                    span = company1.find('span')
                    if span:
                        company.append(span.text)

        footer_card = soup.find_all('div',class_="card-footer py-2")
        [views.append(view1.text) for view in footer_card for view1 in view.find_all('span',class_="text-primary mr-2")]
        sleep(randint(2,6))

data_extract()


#Function for transforming and cleaning the extracted data
def data_transform():

    cleaned_title = [job.strip() for job in titlelist]
    cleaned_company =[companys.strip() for companys in company]
    cleaned_view = [view.replace('Views: ','').strip() for view in views]

    return cleaned_title, cleaned_company, cleaned_view

# Dictionary
dict_job = {'job title': data_transform()[0] ,'Company':data_transform()[1],'View':data_transform()[2]}


# Function for loading the data in excel format
def data_load():
    df = pd.DataFrame(dict_job)
    df.to_excel('job.xlsx')
    return df
print(data_load())









>>>>>>> new
