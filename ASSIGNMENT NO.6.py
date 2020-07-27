#!/usr/bin/env python
# coding: utf-8

# In[12]:


#ASSIGNMENT NO.6
#Convertto a dictonary in line  
list1 = [1,2,3,4,5,7,8]
list2 = ["a","b","c","d","e"]

print("list1 ==>",list1)
print("list2 ==>",list2)

res = {} 
for key in list1: 
    for value in list2: 
        res[key] = value 
        list2.remove(value) 
        break 
print ("Resultant dictionary ==> " +  str(res)) 
       


# In[ ]:




