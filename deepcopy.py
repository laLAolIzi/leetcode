import  copy
#浅copy
a=[1,2,[3,4,]]
b=a.copy()
b[2].append(5)
print(a)
print(b)
#deepcopy
a=[1,2,[3,4,]]
b=a.deepcopy()
b[2].append(5)
print(a)
print(b)