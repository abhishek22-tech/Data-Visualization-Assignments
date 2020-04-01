#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
Location = "C:/Users/abhis/Desktop/Spring 2020/Data Visualization/DataSets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
bins = [0,80,100]
group_names = ['Fail', 'Pass']
df['Pass/Fail'] = pd.cut(df['grade'], bins,        labels=group_names)
df


# In[13]:





# In[14]:





# In[ ]:





# In[ ]:




