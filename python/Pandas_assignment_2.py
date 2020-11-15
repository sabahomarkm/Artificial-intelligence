#!/usr/bin/env python
# coding: utf-8

# In[86]:


import pandas as pd


# In[106]:


df1=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv',sep=',')
df1


# In[88]:


#Convert the type of the column Year to datetime64
df1['Year']=pd.to_datetime(df1.Year,format='%Y')


# In[89]:


#Set the Year column as the index of the dataframe
df2=df1.set_index("Year")
df2.head()


# In[90]:


#Return the first 3 rows of the DataFrame df.
df1.head(3)


# In[91]:


#Select just the 'Murder' and 'Robbery' columns from the DataFrame df and print first 5 rows
df4=df1[['Murder','Robbery']]
df4.head(5)


# In[94]:


#Select the data in rows [3, 4, 8] and in columns ['Murder', 'Robbery']
df1[['Murder','Robbery']].iloc[[3,4,8]]


# In[95]:


#Select only the rows where the number of murder is greater than 24,000
df1[df1['Murder']>24000]


# In[101]:


#Select the rows the murder is between 20k and 24k (inclusive)
df1[df1['Murder'].between(20000,24000)]


# In[110]:


#Calculate the mean murder for each different year in df.
df1.groupby('Year')['Murder'].mean()


# In[104]:


#Sort dMurder first by the values in the 'Murder' in decending order, then by the value in the 'Violent'column in ascending order.
df1.sort_values(by='Murder',ascending=False)


# In[105]:


df2.sort_values(by='Violent',ascending=True)

