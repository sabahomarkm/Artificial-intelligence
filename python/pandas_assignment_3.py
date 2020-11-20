#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd


# In[77]:


df1=pd.read_csv("https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv",sep=',')
df1


# In[93]:


#1.Get the Metadata from the above files.
df1.info()


# In[79]:


#2.Get the row names from the above files.
list(df1.index)


# In[80]:


#3.Change the column name from any of the above file and store the changes made permanently.
df1.rename(columns={'Country':'country'},inplace=True)
df1.head()


# In[81]:


#4.Change the names of multiple columns.
df2=df1.rename(columns={'Indicator':'indicator','Year':'year'})
df2


# In[82]:


#5.Arrange values of a particular column in ascending order.
df1.sort_values(by='Display Value',ascending=False)
df1.head()


# In[104]:


#6.Arrange multiple column values in ascending order.
df1.sort_values(['Year','Display Value'], ascending=[True,True])


# In[84]:


#7.Make country as the first column of the dataframe.
df3=df2.set_index('country')
df3


# In[85]:


#8.Get the column array using a variable
lst=df1.columns.values
lst


# In[86]:


#9.Get the subset rows 11, 24, 37
df1.iloc[[11,24,37]]


# In[87]:


#10.Get the subset rows excluding 5, 12, 23, and 56
exclude=df1.index.isin([5,12,23,56])
df3=df1[~exclude]
df3.head(57)


# In[88]:


#11.find rows with NaN values
df4=df1[pd.isnull(df1).any(axis=1)]
df4.head()


# In[91]:



#12.show rows from dataset 1 country = india with high income
df5=df1[df1['country'].str.match('India')]
df6=df5[df5['World Bank income group'].str.match('High-income')]
df6


# In[94]:


#second set
df10=pd.read_csv("https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv",sep=',')
df10.head()


# In[96]:


#1.Get the Metadata from the above files.
df10.info()


# In[101]:


#2.Get the row names from the above files.
list(df10.index)


# In[102]:


#3.Change the column name from any of the above file and store the changes made permanently.
df10.rename(columns={'Date':'date'},inplace=True)
df10.head()


# In[103]:


#4.Change the names of multiple columns.
df11=df10.rename(columns={'STATION_NAME':'Station_Name','STATION':'STATION_ID'})
df11


# In[106]:


#6.Arrange multiple column values in ascending order.
df13=df10.sort_values(['PRCP','TMIN'], ascending=[True,True])
df13


# In[107]:


#8.Get the column array using a variable
lst=df10.columns.values
lst


# In[108]:


#9.Get the subset rows 11, 24, 37
df1.iloc[[11,24,37]]


# In[109]:


#10.Get the subset rows excluding 5, 12, 23, and 56
exclude=df10.index.isin([5,12,23,56])
df13=df10[~exclude]
df13.head(57)


# In[111]:


#11.find rows with NaN values
df14=df10[pd.isnull(df10).any(axis=1)]
df14.head()

