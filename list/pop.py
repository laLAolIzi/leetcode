#相当于砍掉头
a=[1,2,3,4,8,9]
for _ in range(len(a)):
    b=a.pop(0)
    print(b,len(a))
print(a)
'''
1 5
2 4
3 3
4 2
8 1
9 0
[]
'''
#list.remove(obj)移除列表中某个值的第一个匹配项
b=[1,2,3]
b.remove(2)
print(b)