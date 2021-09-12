#插入排序，二分查找的过程没有必要。从右往左，一边比较一边移动就好了，反正是要移动的。不用先二分查找再插入
import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        if not self.store:
            self.store.append(num)
        else:
            bisect.insort_left(self.store, num) # 插入

    def findMedian(self) -> float:
        n = len(self.store)
        if n & 1 == 1:  # n是奇数
            return self.store[n // 2]
        else:
            return (self.store[n // 2] + self.store[n // 2 - 1]) / 2
