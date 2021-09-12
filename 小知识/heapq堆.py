#python的heapq模块,默认是小根堆
import heapq
#heapq.heappush(heap,item)
h=[7,6,5,4,3,2,1]
heapq.heapify(h)#h变为小根堆
print('test1:',h,type(h))#test1: [1, 3, 2, 4, 6, 7, 5] <class 'list'>
heapq.heappush(h,1)#加入1
print(h)#[1, 1, 2, 3, 6, 7, 5, 4]
print('-----------------------')
#heapq.heappop(heap) 删除堆顶，即最小值
a=heapq.heappop(h)#有返回值
print('test2:',h,a)
