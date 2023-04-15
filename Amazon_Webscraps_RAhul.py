#!/usr/bin/env python
# coding: utf-8

# # Noise Smartwath Data scraps

# In[1]:


#importing modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#getting url from driver
driver = webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.get("https://www.amazon.in")
driver.maximize_window()
#try to access searchbox
search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.clear()

#send key as search 'smartwach'
search_box.send_keys("smart watch")

#click on search button
driver.find_element(By.ID,"nav-search-submit-button").click()

#in filter, i want list only 'Noise company'
driver.find_element(By.XPATH,"//span[text()='Noise']").click()

#getting all element in page by x-path
smartwachs=driver.find_elements(By.XPATH,'//span[@data-component-type="s-search-results"]')

#now, scraps watch models by class and append as in list
watch_model= []
for n in smartwachs:
    names=n.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')
for x in names:
    watch_model.append(x.text)

#now, scraps watch prices by class and append as in list
watch_price= []
price=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for x2 in price:
    watch_price.append(x2.text)   

#now, scraps watch Estimated date of delivery by class and append as in list
estimated_date= []
date=driver.find_elements(By.XPATH,'//span[@class="a-color-base a-text-bold"]')
for x4 in date:
    estimated_date.append(x4.text)

#now, scraps watch total numbers of reviewed of delivery by class and append as in list
total_number_reviewed= []
review=driver.find_elements(By.XPATH,'//span[@class="a-size-base s-underline-text"]')
for x5 in review:
    total_number_reviewed.append(x5.text)


# In[2]:


#here as we see model name is too long length so we slice it.
model=[]
for l in watch_model:
    model.append(l[0:45])


# In[3]:


#now check lenght of all elements by if condtional


# In[4]:


if len(model)==len(watch_price)==len(estimated_date)==len(total_number_reviewed):
    print('we have same lengths of elements')


# In[5]:


#make pandas dataframe of columns
import pandas as pd
dataset=pd.DataFrame(zip(model,watch_price,total_number_reviewed,estimated_date),columns=['Watch_model','Watch_price','Total_number_of_reviews','Delivery_estimated_date'])


# In[6]:


watch_df=dataset.head(24)
watch_df


# In[7]:


#save it excel file
watch_df.to_excel(r"D:\DS\Internship\Noise_smartwatch.xlsx",index=False)
driver.quit()

