import numpy as n
arr = n.arange(10)

a = arr % 2 == 0
print(a)

print(arr[arr % 2 == 0])

b = (arr % 3== 0) & (arr<10)
print(b)

print(arr[(arr % 3== 0) & (arr<10)])