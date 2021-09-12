class Solution:
    def reverse(self, x: int) -> int:
        minnum, maxnum = -2 ** 31, 2 ** 31 - 1

        sign = 1
        if x < 0:
            sign = -1
            x = -x
        s = []
        while x:
            tmp = x % 10
            s.append(tmp)
            x = x // 10
        sum = 0
        for i in s:
            sum = sum * 10 + i
            if sum < minnum or sum > maxnum: return 0
        return sum * sign
