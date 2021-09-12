#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self,head: ListNode, k: int) -> ListNode:

        #(ListNode)h = t = head
        h:ListNode
        t:ListNode
        h=t=head
        while k > 1:
            h = h.next
        while h.next:
            h = h.next
            pre = t
            t = t.next
        pre.next = None
        return t

    a=getKthFromEnd([1, 2, 3, 4, 5],2)
    print(a)

