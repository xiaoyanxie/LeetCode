# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, number):
            number = (number << 1) | node.val
            if not node.left and not node.right:
                return number
            
            total = 0
            if node.left:
                total += dfs(node.left, number)
            if node.right:
                total += dfs(node.right, number)
            
            return total
        
        return dfs(root, 0)
