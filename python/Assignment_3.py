#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q1: Write a function calculation() such that it can accept two variables as arguments and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
def calculation(a,b):
    add=a+b
    sub=a-b
    return(add,sub)
calculation(15,23)


# In[12]:


#Q2 : Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
def showEmployee():
    emp_name=input("Pleas Enter Employee name")
    emp_salary=input("Pleas Enter Employee Salary")
    print('Employee name : ',emp_name)
    if emp_salary=="":
        print("Employee salary:9000")
    else:
        print("Employee salary:",emp_salary)
showEmployee()


# In[26]:


#Q3 : Write a function called multipleLetterCount. This function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the value being the count of the letter.
# Example output:
# multipleLetterCount('awesome') 
# {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

dict={}

def multipleLetterCount(str):
    for i in str:
        dict[i]=str.count(i)
    print(dict)      
multipleLetterCount("awesome")  
    

