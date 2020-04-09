#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
Location = "C:/Users/abhis/Desktop/Spring 2020/Data Visualization/DataSets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df2 = df.take(np.random.permutation(len(df))[:500])
df2


# In[ ]:




