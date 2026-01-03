# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        path = [root.val]
        stack = [(root, root.val, path)]

        while stack:
            node, psum, path = stack.pop()
            if not node.left and not node.right:
                if psum == targetSum:
                    res.append(path)
            if node.left:
                stack.append((node.left, psum + node.left.val, path + [node.left.val]))
            if node.right:
                stack.append((node.right, psum + node.right.val, path + [node.right.val]))

        return res
