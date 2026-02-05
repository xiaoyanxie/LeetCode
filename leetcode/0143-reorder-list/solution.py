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
        # [1,2,3,4,5]
        #      s
        #          f

        # [1,2,3,4]
        #      s
        #        f

        # reverse the second half
        slow = head
        fast = head
        while fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next

        # [1,2,3]
        #    s
        #      f
        if not slow.next:
            return head

        #        n
        #<-4<-5
        #        c
        #     p
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        # intreleave the second half with the first half
        #       n1
        # 1->4->2->3
        #       h1
        #   h2
        # 
        #   n2
        head1 = head
        head2 = prev
        while head2:
            nxt1, nxt2 = head1.next, head2.next
            head1.next = head2
            head2.next = nxt1
            head1, head2 = nxt1, nxt2
        
        return head


