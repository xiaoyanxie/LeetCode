# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        
        count = 0
        for l in lists:
            if not l:
                continue
            heapq.heappush(heap, (l.val, count, l))
            count += 1
        
        dummy = ListNode()
        cur = dummy
        while heap:
            v, cnt, l = heap[0]
            heapq.heappop(heap)
            cur.next = l
            cur = cur.next
            l = l.next
            if l:
                heapq.heappush(heap, (l.val, cnt, l))
        return dummy.next
            
