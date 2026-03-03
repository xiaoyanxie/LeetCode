# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Edge cases:
        (3)
        (3) <-> (2)
        (3) points to self

        [3] -1
         s
           f
        
        [3, 2] 0
         s
         f
        
        [3] 0
         s
         f

        [3, 2] 1
            s
            f

        1 -> end
        2 -> start
        3 -> end
        4 -> start
        5 -> 

        total: 3
        [3,2,0,1] 1
               s
               f
        
        total: 2
                         | 
        [-1,-7,7,-4,19,6,-9,-5,-2,-5]
                          s
                                f
        """
        
        # visited = set()
        # while head:
        #     if head in visited:
        #         return head
        #     visited.add(head)
        #     head = head.next

        """
        a1, a2, a3, ..., aN, c1, c2, c3, c4, ..., meet , ..., cM
        |--------- L1 --------|
                              |-------- L2 --------|
                              |---------------- C -------------|
        
        fast pointer is twice as fast:
        2(L1 + L2) = L1 + L2 + nC
        L1 + L2 = nC
        L1 = nC - L2

        which means: 
        distance from head to cycle start (L1) is equal to the distance from meet point to cycle start (nC - L2)
        """

        slow, fast = head, head
        meet = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                # L1 = nC - L2
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
