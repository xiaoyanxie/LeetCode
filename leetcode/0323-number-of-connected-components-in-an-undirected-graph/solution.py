class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if n == 1:
        #     return n 
        # adj = collections.defaultdict(list)
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # def dfs(i):
        #     visited.add(i)
            
        #     for ele in adj[i]:
        #         if ele not in visited:
        #             dfs(ele)

        # visited = set()
        # count = 0
        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         count += 1
        
        # return count
        parent = list(range(n))
        self.count = n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                parent[rootX] = rootY
                self.count -= 1
                return True
            return False
        
        for u, v in edges:
            union(u, v)

        return self.count

