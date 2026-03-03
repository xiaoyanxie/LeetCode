"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
                    1
              2          3
           4     5    6        7
        8    9 10 11 12 13  14 15

        1. if not parent or node == parent.left:
             node.left.next = node.right
        2. if parent and node == parent.right:
             node.next = parent.next.left
             node.left.next = node.right

        
        """
        prev, curr = root, root # 8, 8
        while curr:
            # iterate curr horizontally
            if curr.left:
                curr.left.next = curr.right
            if curr.next:
                if curr.right:
                    curr.right.next = curr.next.left
                curr = curr.next
            else:
                prev, curr = prev.left, prev.left

        return root
        """
        Time: O(N)
        Space: O(H)
        """
        # def dfs(parent, node): # 6, 13
        #     if not node:
        #         return
        #     if parent and node == parent.right and parent.next:
        #         node.next = parent.next.left
            
        #     if not node.left:
        #         return
        #     node.left.next = node.right

        #     dfs(node, node.right)
        #     dfs(node, node.left)
        
        # dfs(None, root)

        # stack = [(None, root)]
        # while stack:
        #     parent, node = stack.pop()
        #     if not node:
        #         break
        #     if parent and node == parent.right and parent.next:
        #         node.next = parent.next.left
            
        #     if not node.left:
        #         continue
        #     node.left.next = node.right
        #     stack.append((node, node.left))
        #     stack.append((node, node.right))
        # return root
