# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = ListNode()
        curr = root
        while l1 or l2:

            add = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if add >= 10:
                add -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(add)
            curr.next = node
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            curr.next = ListNode(carry)

        return root.next
