#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import glob
all_data = pd.DataFrame()
for f in glob.glob("C:/Users/abhis/Desktop/Spring 2020/Data Visualization/DataSets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)    
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()
all_data.head()


# In[11]:





# In[ ]:





# In[ ]:





# In[ ]:




