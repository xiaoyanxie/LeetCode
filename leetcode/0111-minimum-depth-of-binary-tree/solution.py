# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #use dfs to find the shortest path
        # if not root:
        #     return 0

        # mindep = float('inf')
        # stack=[(root,1)]     

        # while stack:
        #     node, dep = stack.pop()
        #     if not node.left and not node.right:
        #         mindep = min(mindep,dep)
        #     if node.right:
        #         stack.append((node.right,dep + 1))
        #     if node.left:
        #         stack.append((node.left,dep + 1))
            
        # return mindep  

        #use bfs to find the path length to the first childrenless node
        if not root:
            return 0
        queue = deque()
        queue.append((root,1))  
        
        while queue:
            node, dep = queue.popleft()
            if not node.left and not node.right:
                return dep
            if node.right:
                queue.append((node.right,dep + 1))
            if node.left:
                queue.append((node.left,dep + 1))
                        

# It depends on the topology of the tree. If the tree is very deep, use BFS to save sapce. If the tree is wide and shallow, use DFS to save space. If the tree is perfect binary tree(every level is full), height = logN, width = N/2, use DFS to save space. If the tree is slanted, BFS is a better choice which uses O(1) extra space instead of O(N) for DFS.
