# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return head.next
        
        cnt = 0
        dummy = head
        while dummy:
            cnt += 1
            dummy = dummy.next

        if n == cnt:
            tmp = head.next
            head.next = None
            return tmp
            
        idx = cnt - n
        i = 0
        dumm = head
        while dumm and dumm.next:
            if i == idx - 1:
                pre = dumm
                cur = dumm.next
                nxt = dumm.next.next
                pre.next = nxt
                cur.next = None
            if dumm:
                dumm = dumm.next
                i += 1
            else:
                return head
        return head
