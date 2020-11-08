#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


#print first 5 records
df1=pd.read_table(r"https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")
df1.head()


# In[4]:


#print last 7 record
df1.tail(7)


# In[10]:


# print total records and type of variables
df1.info()


# In[5]:


#Print the name of all the columns.
for col in df1.columns: 
    print(col) 


# In[17]:


#How is the dataset indexed?
df1.index


# In[6]:


#Which was the most ordered item? and How many items were ordered?

itemname=df1.groupby('item_name')
df2=itemname.sum() 
df3=df2.sort_values('quantity',ascending=False)
df3.head(1)


# In[7]:


#What was the most ordered item in the choice_description column?
choice=df1.groupby('choice_description')

df3=choice.sum()
df3
df4=df3.sort_values('quantity',ascending=False)
df4.head(1)


# In[8]:


#Turn the item price into a float
def getprice(strprice):
    strtemp=strprice[1:]
    return float(strtemp)

df1['pricenew']=df1['item_price'].apply(getprice)
df1


# In[9]:


#print a data frame with only two columns item_name and item_price
df1[['item_name','item_price']]


# In[10]:


# delete the duplicates in item_name and quantity

df1.drop_duplicates(['item_name','quantity'])


# In[11]:


# select only the products with quantity equals to 1

df1[df1['quantity']==1]


# In[12]:


# select only the item_name and item_price columns
df1[['item_name','item_price']]


# In[18]:


# sort item from the most to less expensive

expensive=df1.groupby('item_name')
df2=expensive.sum()
df3=df2.sort_values('pricenew',ascending=False)
df3.head()


# In[20]:


#What was the quantity of the most expensive item ordered?
df4=df3[['quantity','pricenew']]
df4.head(1)


# In[21]:


#How many times were a Veggie Salad Bowl orded

vsb=df1[df1.item_name == "Veggie Salad Bowl"]
df5=vsb.sum()
df6=df5[['quantity']]
df6

