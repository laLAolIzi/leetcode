#list中的所有函数对原列表操作，不需要a=res.reverse()，因为他返回值为0，就像append函数


res=[1,2,3,4]
a=res.reverse()
res.reverse()
print(a)#None
print(res)