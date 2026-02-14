# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, lower, upper):
            if not node:
                return True
            if upper <= node.val or node.val <= lower:
                return False
            
            return isValid(node.left, lower, node.val) and isValid(node.right, node.val, upper)
        return isValid(root, -inf, inf)
