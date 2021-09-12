'''class Solution:
    def findNumberIn2DArray( matrix: [[int]], target: int) -> bool:
        i=j=0#遍历到二维数组的位置
        m=len(matrix)
        n=len(matrix[0])
        while j<n and matrix[0][j]<target:
            j+=1
        b=j-1#目标所在列
        while matrix[i][b]<target and i<m-1:
            i+=1
        if matrix[i][b]==target:return True
        return False
    a=findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)
    print(a)'''
class Solution:
    def findNumberIn2DArray( matrix: [[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:return  False
        rows=len(matrix)
        cols=len(matrix[0])
        row,col=0,cols
        while row<rows and col>=0:
            if matrix[row][col]>target:
                col-=1
            if matrix[row][col]<target:
                row+=1
            if matrix[row][col]==target:
                return  True
        return False
