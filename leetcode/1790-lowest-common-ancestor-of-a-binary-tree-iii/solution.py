"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        # pathP = set()

        # while p:
        #     pathP.add(p)
        #     p = p.parent
        # while q:
        #     if q in pathP:
        #         return q
        #     q = q.parent
        a = p
        b = q
        while a != b:
            if not a:
                a = q
            else:
                a = a.parent
            if not b:
                b = p
            else:
                b = b.parent
        
        return a
