#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
Location = "C:/Users/abhis/Desktop/Spring 2020/Data Visualization/DataSets/gradedata.csv"
df = pd.read_csv(Location)
#df.drop_duplicates(['name'], keep='last')
df = df.sort_values(by=['fname','age','grade'],ascending=[True, True, True])
df


# In[ ]:




