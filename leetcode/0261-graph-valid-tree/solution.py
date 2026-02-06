class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # roots = n
        parent = list(range(n))
        def find(num):
            if parent[num] != num:
                parent[num] = find(parent[num])
            return parent[num]

        def union(a, b):
            # nonlocal roots
            pA, pB = find(a), find(b)
            if pA == pB:
                return False
            parent[pA] = pB
            # roots -= 1
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return False
        # return roots == 1
        return True
