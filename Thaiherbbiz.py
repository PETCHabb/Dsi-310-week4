#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install openpyxl')


# In[3]:


import pandas as pd
import bs4
import requests
import openpyxl


# In[4]:


data = requests.get('https://www.thaiherbbiz.com/')
soup = bs4.BeautifulSoup(data.text)
name_list = []
code_list = []
price_list = []


# In[5]:


herb = soup.find('div',{'class':'productDetail'})


# In[6]:


name = herb.find('div',{'class':'product_name'})


# In[7]:


name.find('a').text


# In[8]:


code = herb.find('div',{'class':'product_code'})


# In[9]:


code.find('span').text


# In[10]:


price = herb.find('div',{'class':'product_price has_currency_unit'})


# In[11]:


price.get('realprice')


# In[12]:


for c in soup.find_all('div',{'class':'productDetail'}):
    name_list.append(c.find('div',{'class':'product_name'}).find('a').text)
    code_list.append(c.find('div',{'class':'product_code'}).find('span').text)
    price_list.append(c.find('div',{'class':'product_price has_currency_unit'}).get('realprice'))


# In[13]:


table = pd.DataFrame([name_list,code_list,price_list]).transpose()
table.columns = ['name','code','price']
table.set_index('name')


# In[14]:


table.to_excel('Herb Products.xlsx',engine = 'openpyxl')


# In[ ]:





# In[ ]:





# In[ ]:


name_list


# In[ ]:


code_list


# In[ ]:


price_list


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




