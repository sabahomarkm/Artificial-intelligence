#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Q1 : create a txt file, enter multiple lines of text. read this file line by line and store it into a list.
#Apply exception handling technique
try:
    fh=open("file4.txt",'w+')
    fh.write("line1\n line2\n line3")
    lst1=[]
    lst1=fh.readlines()
    print("Write successful")
except:
    print("Try block has some issue")


# In[6]:


#Q2: Write a Python program to write below list content to a file. Apply exceptionhandling technique
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
op1=open("colors.txt",'w')
for i in color:
    op1.write(i+"\n")
    
try:
    rd=open("colors.txt")
    lst1=rd.readlines()
    print(lst1[2])
except IndexError as error:
    print("index not found")


# In[17]:


#Q3 : create a txt file, enter multiple lines of text. remove newline characters from 
#created file and print as a list. Apply exception handling techniques wherever 
#possible
try:
    myfile=open("file3.txt",'w+')
    myfile.write("Line1 \nLine2 \nLine3 \nLine4")
    myfile.seek(0)
    oldlist=myfile.readlines()
    newlist=[]
    for item in oldlist:
        newlist.append(item.rstrip("\n"))
    print(newlist)
except:
    print("Error in try block")
else:
    print("Succesfull")


# In[26]:


#Q4 : create a testfile1.txt file, enter multiple lines of text . Now copy contents of 
#testfile1.txt to new file testfile22.txt. Apply exception handling techniques 
#wherever possible
try:
    myfile1=open("file4.txt",'w+')
    myfile2=open("file5.txt",'w+')
    myfile1.write("Line1 \nLine2 \nLine3 \nLine4")
    myfile1.seek(0)
    list1=myfile1.readlines()
    myfile2.write(str(list1))
except:
    print("Error in try block")
else:
    print("Succesfull")   

