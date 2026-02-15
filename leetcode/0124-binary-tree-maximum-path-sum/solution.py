# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = -inf
        def dfs(node):
            nonlocal maxsum
            if not node:
                return 0
            
            lsum = max(dfs(node.left), 0)
            rsum = max(dfs(node.right), 0)
            pathsum = lsum + node.val + rsum
            maxsum = max(maxsum, pathsum)
            return max(lsum + node.val, rsum + node.val)
        dfs(root)
        return maxsum
