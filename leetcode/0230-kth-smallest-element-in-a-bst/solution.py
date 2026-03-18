# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = 0
        def inOrder(root):
            if not root:
                return
            # if self.k == 0:
            #     return 

            inOrder(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            inOrder(root.right)
        
        inOrder(root)
        return self.res
