import pandas as pd
import numpy as np
import random as r

rand = np.random.randint(1,100,size=(5,5))
rand2 = pd.DataFrame(rand,index= ["a","b","c","d","e"],columns=["f","g","h","i","j"])
print(rand2)

''' 01 to get only column values with index'''
print(rand2["h"])
print(rand2[["f","h","i"]])

''' 02 to get only rows values with index '''
print(rand2.loc["c"])
print(rand2.loc[["a","c","e"]])
print(rand2.iloc[2])