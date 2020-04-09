#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
Location = "C:/Users/abhis/Desktop/Spring 2020/Data Visualization/DataSets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[9]:



import statsmodels.formula.api as sm 
result = sm.ols(formula='grade ~ exercise + hours',data=df).fit()
result.summary()


# In[10]:



df['genderint'] = np.where(df['gender']=='female',1, 0 )
df.head()


# In[11]:


import statsmodels.formula.api as sm 
result = sm.ols(formula='grade ~ genderint + exercise + hours',data=df).fit()
result.summary()


# In[12]:


#grade = 1.917 * hours of study +.984 * hours of exercise+ 0.4476* gender + 58.3145.
#We converted the gender to int and added it to the regression model, we can see that the p-value is 7% but we would like to 
#it below 5% ,  so the only variable that stands out is the genderint with 44.8 percent. so we can leave out genderint variable.


# In[ ]:




