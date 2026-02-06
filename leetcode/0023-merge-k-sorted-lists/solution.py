import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # [1,4,5],
        # [1,3,4],
        # [2,6]
        
        heap = [] # 
        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(heap, [node.val, i, node.next])

        dummy = ListNode() # 1->1->2->3->4->4->5->6
        curr = dummy
        while heap:
            num, i, nxt = heapq.heappop(heap) # [6, 2, 1]
            curr.next = ListNode(num)
            curr = curr.next
            if nxt:
                heapq.heappush(heap, [nxt.val, i, nxt.next])
        
        return dummy.next
