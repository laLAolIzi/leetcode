'''
https://www.cnblogs.com/lwp-king666/p/8331508.html 关于collection模块，提供除了基本数据类型number、set、str、list、tuple、dict
deque双端队列支持线程安全，在双端队列的任何一端执行添加和删除操作，它们的内存效率几乎相同（时间复杂度为O(1)）。
list列表append(0,val)时时间复杂度O(n)，同理pop(0)
deque是为了在两端高效实现插入和删除操作的双向列表，适合用于队列和栈
总之为了双端插入删除元素
'''
import collections

#双端队列会降低时间，但是要注意初始化时不能给单个元素，或者直接给可迭代元素如列表，其实相当于一个函数把list->deque
a=collections.deque([1,2])
print(a)
#deque([1, 2])
a.appendleft(0)#左端加0
a.append(2)
a.pop()
print(a)
#deque([0, 1, 2])
a.popleft()
print(a)
#deque([1, 2])