# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        @cache
        def hashTree(tree):
            if not tree:
                return hash(None)
            return hash( (tree.val, hashTree(tree.left), hashTree(tree.right)) )

        def hasSubRoot(node):
            if not node:
                return False
            if hashTree(node) == hashTree(subRoot):
                return True
            return hasSubRoot(node.left) or hasSubRoot(node.right)
        
        return hasSubRoot(root)
