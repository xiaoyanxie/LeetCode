# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # [1,2,3,4]
        slow = head # [3, 4]
        fast = head # [4]
        while fast.next:
            slow = slow.next
            if not fast.next.next:
                fast = fast.next
            else:
                fast = fast.next.next

        # reverse
        prev, curr = None, slow.next # [4], None
        slow.next = None
        while curr:
            nxt = curr.next # None
            curr.next = prev # 
            prev, curr = curr, nxt

        # interleave
        head1 = head # [1,4,2,3]
        head2 = prev # [4]
        while head2:
            nxt1, nxt2 = head1.next, head2.next # [2,3,4], None
            head1.next = head2
            head2.next = nxt1
            head1, head2 = nxt1, nxt2

        return head
