# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. find the length
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next

        # 2. reverse the first half
        """
        1

        i = 2
      <-3 <- 2    5 -> 2 -> 3
             p.   c

      <- 2   2
         p.  c   
        """
        prev, curr = None, head
        i = 0
        while i < length // 2:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
            i += 1

        # 3. check palindrome
        h1, h2 = prev, curr
        if length % 2 != 0:
            h2 = h2.next

        isPal = True
        while h1 and h2:
            if h1.val != h2.val:
                isPal = False
                break
            h1, h2 = h1.next, h2.next

        # 4. restore the first half
        """
          3 -> 2 -> 5 -> 2 -> 3
     p    c
        """
        while prev:
            nxt = prev.next
            prev.next = curr
            prev, curr = nxt, prev

        assert curr == head

        return isPal
