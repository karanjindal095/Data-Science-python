import pandas as pd
import numpy as np
import random as r

rand = np.random.randint(1,100,size=(5,5))
rand2 = pd.DataFrame(rand,index= ["a","b","c","d","e"],columns=["f","g","h","i","j"])
print(rand2)

''' 01 add new column'''
rand2["New"] = [9,8,7,6,5]
print(rand2)

''' 02 add new row'''
rand2.loc["nava"] = [1,2,3,4,5,6]
print(rand2)

''' 03 delete a column '''
rand3 = rand2.drop("New",axis=1)       #delete column temperary
print(rand3)

rand2.drop("New",axis=1,inplace=True)   #delete column permanently
print(rand2)

'''04 delete a row '''
rand4 = rand2.drop("nava",axis=0)        #delete row temperary
print(rand4)

rand2.drop("nava",axis=0,inplace=True)    #delete row permanently
print(rand2)