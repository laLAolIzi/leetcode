
'''
1 查：print(dic3['fond'])   # 找到'键':fond

2 增，改：dic3['grilFriend'] = '小花'  

有的话，修改，没有的话，增加。 可以给添加上去，跟上面写的方式是一样的
3 删：dic3.pop('key'),例子：dic3.pop('grilFriend')  # 删除指定元素

4 打印键值：print（dic3.keys()）,print(dic3.values())

5 判断是否在字典里： 注意是keys() 和values()

if 'fonds' in dic3.keys():

if '小明' in dic3.values():
#python中的字典就像java的hashmap，键值对
import collections

s = "loveleetcode"
# build hash map : character and how often it appears
count = collections.Counter(s)
print(count)

'''
test={'a':1}
print('a' in test)
test['b']=2
print(test)#{'a': 1, 'b': 2}
for k,v in enumerate(test):
  print(k,v)#0 a 1 b
for k, v in test.items():#items() 方法以列表返回可遍历的(键, 值) 元组数组。
  print(k, v)#a 1  b 2
#print('a' in test)#True test.keys()一样
#print(1 in test.values())#True  与test不一样

a={'a':1,'b':2}
#items()函数是dict的特有函数
#字典遍历只能通过调用for k,v in dict.items():，此时只可以修改value值，key修改不了
for k,v in a.items():
    #print(k, v)
    v+=1
    print(k, v)
    #k='gai'
#print(a['a'])
#enumerate（(枚举）函数，将可迭代对象变为，(索引 数据)的格式，只可以遍历不可修改
for i,j in enumerate(a):
    print(i,j)