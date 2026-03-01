# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        [[1,4,5],[1,3,4],[2,6]]
          ^
        
        heap = (), (), ()


        """
        minheap = []
        for i, head in enumerate(lists):
            if not head: continue
            heapq.heappush(minheap, (head.val, i))
        
        dummy = ListNode() # -> (1) -> (1) -> (2) -> (3) -> (4) -> (4) -> (5) -> (6)
        curr = dummy
        while minheap:
            val, i = heapq.heappop(minheap) # 6, 2, None
            curr.next = ListNode(val)
            curr = curr.next

            nxt = lists[i].next
            if nxt:
                heapq.heappush(minheap, (nxt.val, i))
                lists[i] = lists[i].next

        return dummy.next
