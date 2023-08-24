import pandas as pd
import numpy as np
import random as r

rand = np.random.randint(1,100,size=(5,5))
print(rand)

rand2 = pd.DataFrame(rand)
print(rand2)

rand3 = pd.DataFrame(rand,index= ["a","b","c","d","e"],columns=["f","g","h","i","j"])
print(rand3)