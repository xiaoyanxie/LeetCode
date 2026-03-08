# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        #pre->b->a-> post
        #
        #
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next

            a.next = b.next
            b.next = a
            pre.next = b

            pre = a
        return dummy.next


