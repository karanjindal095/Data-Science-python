import numpy as n
unsort = n.array([5,7,4,9,2,0])
unsort_1 = n.array([6,9,3,9,0,1,4,7,2,1,0])
sort = n.sort(unsort)
sort_1 = n.sort(unsort_1)
print(sorted(unsort))  #sorted(array) = accending order
print(sort)
print(sort_1)

''' 02 copy() '''
new = unsort.copy()
print(new)