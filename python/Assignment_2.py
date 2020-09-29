#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Q 1: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
lst1=list(tuple1)
lst1[1][0]=222
lst1


# In[33]:


#Q 2: Count the number of occurrences of item 50 from a tuple
tuple2 = (50, 10, 60, 70, 50)
count=0
lst2=list(tuple2)
for i in  lst2:
    if i==50:
        count+=1
print(count)


# In[8]:


#Q 3: Write a Python program to convert a list to a tuple
x=[1,5,8,7,6,9]
tuple2=tuple(x)
tuple2


# In[34]:


#Q 4: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3=set1.union(set2)
set3


# In[19]:


#Q5: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
dict1


# In[37]:


#Q6: Given a Python dictionary, Change Brad’s salary to 8500
sampleDict = {
 'emp1': {'name': 'Jhon', 'salary': 7500},
 'emp2': {'name': 'Emma', 'salary': 8000},
 'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary']=8500
sampleDict


# In[40]:


#Q7: Rename key city to location in the following dictionary
sampleDict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"
}
oldkey='city'
newkey='location'
sampleDict[newkey]=sampleDict.pop(oldkey)
sampleDict

