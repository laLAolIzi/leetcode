import heapq
#本身是小根堆
class Solution:
    def getMax(self, arr: list, k):
        if k==0:return list()
        h=[-x for x in arr[:k]]#前k个元素取反，取反最小的就是最大的
        heapq.heapify(h)#转为heapq堆
        length=len(arr)
        for i in range(k,length):
            #minh=heapq.heappop(h)

            if -h[0]>arr[i]:#取反就是最大的
                heapq.heappop(h)
                heapq.heappush(h,-arr[i])

        res=[-x for x in h]
        return res
a=Solution()
res=a.getMax([3,2,1],2)
print(res)