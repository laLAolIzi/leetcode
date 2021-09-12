###一个字符类型列表（如刚输入的数字），转化为整形列表
l1=input().split()
l1=[int(cha) for cha in l1]
print(l1)
#输入1 2 3 4 5 6 7，输出[1, 2, 3, 4, 5, 6, 7]

###输入一行数字，分别以int型赋给x，y，z
#22 33 22  空格
#22 33 22
x,y,z=map(int,input().strip().split())
print(x,y,z)
'''getS = lambda x: "" if x <= 1 else "s"
#a=getS(int(input()))
print((getS))'''

###输入n（2）行，每行不限数量，以行为单位组成二维数组
list = []
for i in range(2):
    list.append([int(i) for i in input().split()])#用.extend()则是在一维数组后面增加几个元素
print(list)
#[[1, 2, 3], [1, 2, 2], [1, 5, 8]]
#[12, 3, 112, 3, 3, 3, 11, 1]
###类似上面