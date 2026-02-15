# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        lookup = { num: i for i, num in enumerate(inorder) }
        def build(i, j):
            nonlocal idx
            if idx == len(preorder):
                return None
            
            num = preorder[idx]
            inOrderIdx = lookup[num]
            if not (i <= inOrderIdx <= j):
                return None

            idx += 1
            root = TreeNode(num)
            root.left = build(i, inOrderIdx - 1)
            root.right = build(inOrderIdx + 1, j)
            return root

        return build(0, len(inorder) - 1)
