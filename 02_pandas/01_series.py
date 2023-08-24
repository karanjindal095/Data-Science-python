import pandas as pd
import numpy as np
l1 = [1,2,3,4,5,6]
label = ["a","b","c","d","e","f"]
dis = {"A":10,"B":20,"C":30,"D":40,"E":50}

''' 01 print index and list'''
l2 = pd.Series(l1)  
print(l2)
print(l2[2])    #3

label2 = pd.Series(label)
print(label2)

dis2 = pd.Series(dis)
print(dis2)
print(dis2["C"])  #30
print(dis2[2])    #30

'''02 change data and index'''
l3 = pd.Series(data=l1,index=label)
print(l3)
print(l3["a"])  #1
print(l3[0])    #1

label3 = pd.Series(data=label ,index=l1)
print(label3)
print(label3[2])