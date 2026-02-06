# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def unlink(prev, curr):
            nxt = curr.next
            curr.next = None
            prev.next = nxt
        
        prev = None
        curr = head
        probe = head
        for _ in range(n):
            probe = probe.next
        
        while probe:
            prev, curr = curr, curr.next
            probe = probe.next

        if not prev:
            return curr.next
        else:
            unlink(prev, curr)
            return head

