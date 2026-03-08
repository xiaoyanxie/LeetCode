class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = [ i for i in range(n) ]
        def find(v):
            if v == uf[v]:
                return v
            
            uf[v] = find(uf[v])
            return uf[v]

        def union(v1, v2):
            p1 = find(v1)
            p2 = find(v2)

            if p1 != p2:
                uf[p1] = p2
            
        for v1, v2 in edges:
            union(v1, v2)
        
        return find(source) == find(destination)
