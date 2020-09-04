#!/usr/bin/env python
# coding: utf-8

# In[103]:


#1 Input a string of odd length (minimum 9 characters), print a string made of the 3 middle characters from input string.(eg :- if input is abcdefghi, answer should be def)

str1=input("Please Enter your string: ")
if (len(str1)) % 2 ==0:
    print("condition violated!!Try again ")
elif int(len(str1)<9):
    print("condition violated!! Try again")
else:
    length=int(len(str1)/2)
    str2=str1[length-1:length+2]
    print(str2)


# In[9]:


#2.a Calculate the sum and average of first n natural numbers using for loop
limit=int(input("Please Enter The Limit : "))
sum=0
for i in range(limit):
    sum+=i
    avg=sum/limit
print("Sum of {} and average is {}".format(sum,avg))


# In[53]:


#2.b Calculate the sum and average of first n natural numbers using while loop
limit=int(input("Please Enter The Limit : "))
sum=0
i=0
while i<limit:
    sum+=i
    avg=sum/limit
    i+=1
print("Sum of first {} numbers  are {} and average is {}".format(limit,sum,avg))


# In[106]:


#3 Accept list of 5 float numbers as input from user using loop and store values in a list
list=[]
for i in range(5):
    elements=float(input("Please Enter Elements {} :".format(i+1)))
    list.append(elements)
print(list)


# In[108]:


#4. a program to print pattern
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 """
i=1
for i in range(6):
    for j in range(i):
         print(j+1,end="")  
    print("")


# In[49]:


#4.b program to print pattern
"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
row=5
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")


# In[67]:


#5.input a number, count and print the total number of digits in that number using while loop
length=0
n=int(input("please a enter number"))
while n>0:
    length+=1
    n=n//10
print("the lenght  numbers are {}".format(length))


# In[100]:


#6 Given two lists. Create a third list by picking an odd-index element from the first list and even index elements from second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
lst1=[3,6,9,12,15,18,21]
lst2=[4,8,12,16,20,24,28]
odd_index=lst1[1::2]
even_index=lst2[0::2]
lst3=odd_index+even_index
print(lst3)


# In[88]:


#7 program to get the smallest number from a list.
lst1=[]
limit=int(input("Please enter the list size : "))
for i in range(limit):
    element=int(input())
    lst1.append(element)
k=lst1[0]
for i in range(1,len(lst1)):
    if lst1[i]<k:
        k=lst1[i]
print("the smallest element in the list is :{} ".format(k))


# In[94]:


#Reverse the following list using for loop and range [ do not use reverse or reversed like functions] list1 = [10, 20, 30, 4, 50]
lst1=[10, 20, 30, 4, 50]
k=len(lst1)
lst2=[]
for i in range(k-1,-1,-1):
    lst2.append(lst1[i])
print(lst2)


# In[ ]:




