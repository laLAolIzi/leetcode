a=[[1] * 4]
print(a)#[[1, 1, 1, 1]]
b=[[1] + [0] * (4 - 1) for _ in range(3- 1)]
print(a+b)
'''等于[(  [1] + [0] * (4 - 1)  ) for _ in range(3- 1)]
[[1, 1, 1, 1],
 [1, 0, 0, 0], 
 [1, 0, 0, 0]]
'''
#创建二维数组的正确方法

dp = [[0] * 6 for _ in range(3)]#6列 3行
        # 第一行都赋予 1
m,n=len(dp),len(dp[0])
print(m,n)

for j in range(n):
    dp[0][j] = 1
# 第一列都赋予 1
for i in range(m):
    dp[i][0] = 1

#错误方法,只是指向三个空列表的引用。
a=[[0]*3 ]*6#6行 3列
print(a)
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][1]=2
print(a)
#[[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
