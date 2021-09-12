class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        self.store.append(num)

    def findMedian(self) -> float:
        self.store.sort()
        n = len(self.store)
        if n & 1 == 1: # n 是奇数
            return self.store[n // 2]
        else:
            return (self.store[n // 2 - 1] + self.store[n // 2]) / 2

test=MedianFinder()
test.addNum(1)
print(test.store)