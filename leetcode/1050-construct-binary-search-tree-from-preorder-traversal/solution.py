# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        idx = 0
        def build(lower, upper):
            nonlocal idx
            if idx == len(preorder) or not (lower < preorder[idx] < upper):
                return None

            num = preorder[idx]
            root = TreeNode(num)
            idx += 1
            root.left = build(lower, num)
            root.right = build(num, upper)
            return root

        return build(-inf, inf)
