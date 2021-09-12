class MedianFinder:
    def __init__(self):
        self.A = []

    def addNum(self, num: int) -> None:
        n = len(self.A)
        i, j = 0, n
        while i < j:
            mid = (i + j) // 2
            if num < self.A[mid]:
                j = mid
            else:
                i = mid + 1
        self.A.append(num)
        k=n-1
        while k>=i:
            self.A[k + 1] = self.A[k]
            k-=1
        self.A[i] = num

    def findMedian(self) -> float:
        n = len(self.A)
        if n & 1 == 1:  # n 是奇数
            return self.A[n // 2]
        else:
            return (self.A[n // 2 - 1] + self.A[n // 2]) / 2.0
test=MedianFinder()
test.addNum(-1)
test.addNum(-2)
test.addNum(-3)
test.addNum(-4)
print(test.findMedian())
test.addNum(-5)
print(test.findMedian())
print(test.A)