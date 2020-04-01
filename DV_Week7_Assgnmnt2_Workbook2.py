#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db 
db_file = r'C:/Users/abhis/Desktop/Spring 2020/Data Visualization/DataSets/salesdata.db' 
engine = create_engine(r"sqlite:///{}"
                       .format(db_file)) 
sql = "select name from sqlite_master"    
"where type = 'table';"
test = pd.read_sql(sql, engine)


# In[13]:


print(test.iloc[0])


# In[14]:


sql = 'SELECT * from {};'.format(test.iloc[0].iloc[0])
sales_data_df = pd.read_sql(sql, engine) 
sales_data_df


# In[ ]:





# In[ ]:




