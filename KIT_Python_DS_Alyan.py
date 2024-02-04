#!/usr/bin/env python
# coding: utf-8

# In[10]:


pi= 3.142

radius = float(input("Enter Radius: "))
area = pi * radius**2

print("Area of Circle for "+str(radius)+" radius is: " +str(area))


# In[29]:


def maxnumber(num1,num2):
    if num1 > num2:
        print("Num1 is Greater")
    else:
        print("Num2 is Greater")
        
x,y = input("Enter Num1 and Num2: ").split()

a = int(x)
b = int(y)

maxnumber(a,b)



# In[33]:


num = [1,2,3,4,5,6,7,8]

check = int(input("Enter Number to Check: "))

for i in num:
    if check == i:
        print("It Exists")
        break
    else:
        print("NOT HERE")


# In[34]:


fruits = ['Banana','Oranges','Apple','Guava','Pomegranate']

print(fruits)


# In[35]:


fruits.append('Hemamelon')


# In[36]:


print(fruits)


# In[44]:


Fruits = {1: 'Banana', 2:'Apple',3: 'Oranges'}
print(Fruits)
print(Fruits[1])
print(Fruits)


# In[42]:


MyTuple = ('Yamaha','Suzuki','Kawasaki','Honda',125,650)
print(MyTuple[1])
print(MyTuple[5])


# In[45]:


import pandas as pd


# In[50]:


data = pd.read_excel("C:/Users/KIT/Downloads/YixJih.xlsx")


# In[51]:


data


# In[52]:


data.index

