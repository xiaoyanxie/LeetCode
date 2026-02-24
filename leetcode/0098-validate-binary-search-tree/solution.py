# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, nmin, nmax):
            if not node:
                return True
            if not nmin < node.val < nmax:
                return False
            return isValid(node.left, nmin, node.val) and isValid(node.right, node.val, nmax)

        # if not root:
        #     return True
        return isValid(root, float('-inf'), float('inf'))
        # if not root:
        #     return True
        # if not self.isValidBST(root.left):
        #     return False
        # if root.val <= self.pre:
        #     return False
        # self.pre = root.val
        # return self.isValidBST(root.right)
    

