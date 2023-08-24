import numpy as n                 
a  = n.array([1,2])      # 1d array
a2 = n.array([[1,2,3],[1,2,3]])    # 2d array
a3 = n.array([[[1,2],[3,4]],[[5,6],[7,8]]])    #3d array
a4 = n.array([[[1,2,9],[3,4,8]],[[5,6,7],[7,8,6]],[[11,12,13],[14,15,16]]])   # 3d array 
# print(a,a.ndim,type(a))
# print(a2,a2.ndim)
# print(a3,a3.ndim)
# print(a4,a4.ndim)
# [[[1d]2d]3d]

# print("1d") 
# print(a[0]) #1

# print("2d") 
# print(a2[0,2],a2[1,1]) #3,2
# print(a2[0]) #3,2

# print("3d") 
# print(a3[0,0,1]) #2
# print(a3[1,0]) 
# print(a3[0])
# print(a3[0,1,0]) #3
# print(a3[1,0,1]) #6
# print(a3[1,1,0]) #7

# print("3d") 
# print(a4[0,1,2]) #8
# print(a4[1,0,2]) #7
# print(a4[2,1,1]) #15
print(n.shape(a4))