class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n-1 != len(edges):
            return False
      

        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
       
        visited = set()
        def dfs(node):
            visited.add(node)
            for ele in adj.get(node,[]):
                if ele not in visited:
                    dfs(ele)

            return True

        dfs(0)
        return len(visited) == n
            
            
