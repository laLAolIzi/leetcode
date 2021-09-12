'''
1.正常二分查找，要i<=j(针对只有一个元素的i情况
'''
class zheban:
    def zhebanchazhao(l:list,n:int):
        a=len(l)-1
        i,j=0,a
        while i<=j:
            mid=(i+j)//2
            if l[mid]==n:# and l[mid-1]!=n:找到首个出现数的位置
                return mid
            elif l[mid]<n:
                i=mid+1
            else:
                j=mid-1

    a = zhebanchazhao([1, 10, 35, 36, 55, 61, 89],35)
    print(a)

#查找有序数组中某个数首次出现的位置（也可以找到之后直接向左，时间复杂度稍微高点
class zheban1:
    def shouge(self , n , v , a ):
        i,j=0,n-1
        while i<=j:###
            mid=(i+j)//2
            if a[mid]==v and a[mid-1]!=v:###
                return mid
            elif a[mid]>=v:#当等于v时要调整j而非i
                j=mid-1
            elif a[mid]<v:#小于时向右找
                i=mid+1