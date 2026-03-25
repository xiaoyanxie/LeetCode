# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        carry: 1
        l1 = [2,4,5], l2 = [5,6,4]
                  l1            l2

        root -> node(7) -> node(0) -> node(0) -> node(1)
        """
        carry = 0
        root = ListNode()
        curr = root
        while l1 or l2:
            n = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if n >= 10:
                n -= 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(n)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            curr.next = ListNode(1)
        
        return root.next
