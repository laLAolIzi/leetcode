from node import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

t=Solution()
a=t.middleNode([1,2,3,4,5])
print(a)