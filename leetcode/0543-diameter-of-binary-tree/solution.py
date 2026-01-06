# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node)->int:
            if not node.left and not node.right:
                return 0
            if node.left:
                leftlen = 1 + dfs(node.left)
            else:
                leftlen = 0
            if node.right:
                rightlen = 1 + dfs(node.right)
            else:
                rightlen = 0
            self.maxLen = max(self.maxLen, (leftlen + rightlen))
            return max(leftlen, rightlen)

        self.maxLen = 0

        dfs(root)
        return self.maxLen





        

