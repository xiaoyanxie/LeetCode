# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head = [1] n = 1 fast = 1 slow = 0->fast = None, slow = 1
        if not head:
            return head
        if not head.next:
            return head.next

        dummy = ListNode(0, head)
        fast = dummy
        for _ in range(n+1):
            fast = fast.next
        
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
            
        return dummy.next
        

