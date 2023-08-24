import numpy as n
arr = n.arange(10)
print(arr)
print(arr.shape)
print(arr.reshape(5,2))   #reshape(row,column) r and c should be multiple of shape of arr
print(arr.reshape(5,-1))
print(n.arange(15).reshape(5,3))