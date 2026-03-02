"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
         1---2---3---4---5---6--NULL
                 |
                 7---8---9---10--NULL
                     |
                     11--12--NULL
        """
        if not head:
            return None

        dummy = Node() # 
        curr = dummy 

        stack = [head]
        while stack: # 
            node = stack.pop() 
            curr.next = node
            node.prev = curr
            curr = curr.next

            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
        
        newHead = dummy.next
        dummy.next.prev = None
        return newHead
