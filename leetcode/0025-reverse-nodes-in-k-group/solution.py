# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(prev, node, k) -> Tuple[ListNode, ListNode]:
            """
            cnt: 2
         <- 1 <- 2    3 -> 4
                 p
                      c
            2 -> 1 -> 3 -> 4
            p   
                      c
            """
            curr = node
            while k > 0:
                assert curr
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            node.next = curr
            return prev, curr
        
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next

        groups = length // k
        prev, curr = None, head
        newHead = None
        while groups > 0:
            """
            2 -> 1 -> 3 -> 4
            p   
                      c
            """
            nxtPrev = curr
            prevHead, curr = reverse(prev, curr, k)
            if prev:
                prev.next = prevHead
            prev = nxtPrev
            if not newHead:
                newHead = prevHead
            groups -= 1
        
        return newHead
