import numpy as n

''' 01 shape '''
arr = n.array([1,2,3,4])
print(arr.shape)
print(type(arr.shape))

l1 = [1,2,3]
l2 = [4,5,6]
arr2 = n.array([l1,l2])
print(arr2.shape)

''' 02 zero() '''
print(n.zeros(50))                    #print zeros
print(n.zeros((10,10)))               #zero( (row,column),dtype = float ) 
print(n.zeros((10,10), dtype= int))   #zero((row,column),dtype = int) 

''' 03 ones() '''
print(n.ones(5))                   #print ones
print(n.ones((3,3), dtype= int))   #same as zeros

''' 04 full() '''
print(n.full(10,5))          #full(range,number) print same no. in that range 

''' 05 arange() '''
print(n.arange(1,10))      #range(start,end-1)
