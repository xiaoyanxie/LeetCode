# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #traverse each level using priority queue
        q =deque([(root, 1)])
        max_width = 0
        while q:
            width = 0
            size = len(q)
            node,idx = q[0]
            left = idx
            for i in range(size):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))
                
            width = idx - left + 1
            max_width = max(width, max_width)
        
        return max_width


