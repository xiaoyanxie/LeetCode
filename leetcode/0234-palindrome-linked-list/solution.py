# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # compute length
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        
        # reverse the first half
        i = 0
        prev, curr = None, head
        while i < length // 2:
            i += 1
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        # check palindrome
        p1, p2 = prev, curr
        if length % 2 != 0:
            p2 = p2.next
        
        isPal = True
        while p1 and p2:
            if p1.val != p2.val:
                isPal = False
                break
            p1, p2 = p1.next, p2.next
        
        # restore
        while prev:
            nxt = prev.next
            prev.next = curr
            prev, curr = nxt, prev
        
        return isPal
