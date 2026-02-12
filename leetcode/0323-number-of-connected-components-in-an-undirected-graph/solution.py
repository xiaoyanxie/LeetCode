class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [ i for i in range(n) ]

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            parent[p1] = p2
            return True

        for edge in edges:
            if union(edge[0], edge[1]):
                n -= 1
        
        return n
