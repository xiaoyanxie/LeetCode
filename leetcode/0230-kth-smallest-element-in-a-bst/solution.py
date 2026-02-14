# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nth = 0
        def inorder(node):
            nonlocal nth
            if not node:
                return None
            found = inorder(node.left)
            if found:
                return found
            
            nth += 1
            if nth == k:
                return node
            return inorder(node.right)
        
        return inorder(root).val
