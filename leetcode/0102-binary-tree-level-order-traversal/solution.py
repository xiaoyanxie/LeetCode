# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ordered = []
        currLevel = -1
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            if currLevel < level:
                ordered.append([node.val])
                currLevel = level
            else:
                ordered[currLevel].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return ordered
