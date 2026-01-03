# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            #augmented node, includes sum from root to it
        # match = False
        stack=[(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right:
                if val == targetSum:
                    return True
            if node.left:
                stack.append((node.left, val+node.left.val))
            if node.right:
                stack.append((node.right, val+node.right.val))
        return False


