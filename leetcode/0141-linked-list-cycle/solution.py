# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while head and fast:
            head = head.next
            fast = fast.next.next if fast.next else None
            if head and fast and head == fast:
                return True
        return False
