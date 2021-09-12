#tuple元组不允许修改，删除，但是可以索引，截取
#len  连接(1, 2, 3) + (4, 5, 6)=	(1, 2, 3, 4, 5, 6)  复制 元素是否存在   迭代
a=[5,1,2,3]
b=tuple(a)#转换类型
print(type(b))
print(a[1:])
print(a[0])
c=(1,2)#默认是元组<class 'tuple'>
print(type(c))

#集合
d1=set('123')
d2={1,2,3}
print(type(d1))#<class 'set'>
print(type(d2))#<class 'set'>

print('---------')
#TypeError: can only concatenate list (not "int") to list
#列表拼接要是 列表+列表（int  str不行
a1=a+1
print(a1)
#元组同理，只允许元组+元组
c=c+'a'
print(c)