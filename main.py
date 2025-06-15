from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator #for airflow etl workflow 
import pandas as pd
import requests 
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from datetime import datetime
# List
titlelist = []
company=[]
views=[]
#implementation of airflow in progress 
# Function for Extracting the data from the website using bs4
def data_extract():
    """
    Extracting the job title, company name and view counts from 6 different page of the website  using beautiful soup module with the time delay
    and stores the data in the list for further processing  
    
    :param : None
    :return : None 

    >>> data_extract()
    perform the operation
    """
    
    for page in range(1, 6):

        headerss = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-langauge': 'en-US, en;q=0.5'}
        request = requests.get('https://merojob.com/category/it-telecommunication/?page='+str(page))
        soup = BeautifulSoup(request.content,"lxml")

        title = soup.find_all('div', class_='card-body')
        #iterating through the job title h1
        for each in title:
            [titlelist.append(each2.text) for each1 in each.find_all('h1') for each2 in each1.find_all('a')]

            #iterating through the company name h3 
            for company1 in each.find_all('h3'):
                a = company1.find('a')
                if a:
                   company.append(a.text)
                else:
                    span = company1.find('span')
                    if span:
                        company.append(span.text)
                        
        #iterating through the footer card for view count
        footer_card = soup.find_all('div',class_="card-footer py-2")
        #iterating through the view count span
        [views.append(view1.text) for view in footer_card for view1 in view.find_all('span',class_="text-primary mr-2")]

        sleep(randint(2,6))

data_extract()


#Function for transforming and cleaning the extracted data

def data_transform():
    """
    Transform the current data into cleaned data by removing the whitespaces
    :param:None
    :return : cleaned title, company, and view data in the form of list 

    >>> data_transform()
    perform data transformation 
    """
    # Cleaning the data by removing the whitespaces
    cleaned_title = [job.strip() for job in titlelist]
    cleaned_company =[companys.strip() for companys in company] #  removing the whitespaces from company name
    cleaned_view = [view.replace('Views: ','').strip() for view in views] # removing the 'Views: ' from the view count and stripping the whitespaces

    return cleaned_title, cleaned_company, cleaned_view

# Dictionary for storing the data extracted from scraping
dict_job = {'job title': data_transform()[0] ,'Company':data_transform()[1],'View':data_transform()[2]}


# Function for loading the data in excel format
def data_load():
    """ 
    After data is  collected and transformed, it is converted into pandas dataframe and further loaded in the excel file 
    :param:None
    :return : dataframe 
    """
    df = pd.DataFrame(dict_job)
    df.to_excel('job.xlsx')
    return df
print(data_load())


# initalization of default argument
default_args = {
    'owner': 'airflow'
}
# initializtion of DAG worflow
with DAG(
    dag_id='web_job_scraping_dag',
    default_args=default_args,
    start_date=datetime(2025, 6, 9),
    schedule_interval=None,
    catchup=False
) as dag:


    # extraction task
    extract_task = PythonOperator(
            task_id='extract_task',
            python_callable=data_extract
            
            )
    # transformation task
    transform_task = PythonOperator(
            task_id='transform_task',
            python_callable=data_transform
        )

    #loading Task

    load_task = PythonOperator(
            task_id='load_task',
            python_callable=data_load
        )

# data task flows 
extract_task >> transform_task >> load_task




