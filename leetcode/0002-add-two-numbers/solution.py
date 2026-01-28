# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 = [9,9,9], l2 = [9,9]
        # sumi = 0


        carry = 0 # 1
        dummyHead = ListNode() # () -> (8) -> (9) -> (0) -> (1)
        curr = dummyHead # 
        while l1 or l2:
            if l1 and l2:
                sumi = l1.val + l2.val + carry
            elif l1:
                sumi = l1.val + carry
            else:
                sumi = l2.val + carry
            
            if sumi > 9:
                carry = 1
                sumi = sumi - 10
            else:
                carry = 0
            
            next = ListNode(sumi)
            curr.next = next
            curr = next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry == 1:
            curr.next = ListNode(1)

        return dummyHead.next
