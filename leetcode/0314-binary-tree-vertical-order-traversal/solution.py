# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        def countColumns():
            queue = deque([(root, 0)])
            l, r = 0, 0
            while queue:
                node, i = queue.popleft()
                l, r = min(l, i), max(r, i)
                if node.left:
                    queue.append((node.left, i - 1))
                if node.right:
                    queue.append((node.right, i + 1))
            return l, r
        
        l, r = countColumns()
        # print(f'{l} - {r}')
        ret = [ [] for _ in range(r - l + 1) ] # []
        # print(ret)
        
        def index(i):
            return i - l
        
        queue = deque([(root, 0)]) # 
        while queue:
            node, i = queue.popleft()
            # print(f'assign {node.val} to {index(i)}')
            ret[index(i)].append(node.val)
            if node.left:
                queue.append((node.left, i - 1))
            if node.right:
                queue.append((node.right, i + 1))

        return ret

