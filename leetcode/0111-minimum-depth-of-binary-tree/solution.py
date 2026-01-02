# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        elif root.right == None and root.left != None:
            return self.minDepth(root.left) + 1
        elif root.left != None and root.right != None:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        

