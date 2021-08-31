#!/usr/bin/env python
# coding: utf-8

# In[137]:


def Fibonacci(N):
    
    x1,x2 = 1,1 #Starting values for the Fibonacci sequence
    counter = 0 #Counter to keep track of the length of the sequnce
    
    while counter <= N:  #Loops until each number in the Fib. sequence is calculated based on the users request
        print(x1)
        x1,x2 = x2,x1+x2 #Calculates the following number in the sequence by adding the previous two
        counter += 1     #Adds one to the counter for each loop, up to the desired amount of numbers in the sequence
    

Fibonacci(5)         


# In[ ]:





# In[ ]:





# 
