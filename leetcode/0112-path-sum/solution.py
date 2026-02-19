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
        
        # if not root.left and not root.right:
        #     if root.val == targetSum:
        #         return True
        #     return False
        
        # return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        
        stack =[(root, targetSum-root.val)]
        while stack:
            node, sum = stack.pop()
            if sum == 0 and not node.left and not node.right:
                return True
            
            if node.right:
                stack.append((node.right, sum - node.right.val))
                
            if node.left:
                stack.append((node.left, sum - node.left.val))
            
        return False

            
