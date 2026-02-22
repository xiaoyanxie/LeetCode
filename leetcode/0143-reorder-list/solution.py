# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find median
        slow = head
        fast = head
        if not head or not head.next or not head.next.next:
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        #reverse second half
        pre = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        #add second half to first half
        first = head
        second = pre
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        return head

