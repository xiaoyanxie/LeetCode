class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return n == 1

        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = set([edge[1]])
            else:
                graph[edge[0]].add(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = set([edge[0]])
            else:
                graph[edge[1]].add(edge[0])
        
        visited = set()
        stack = [edges[0][0]]
        while stack:
            i = stack.pop()
            visited.add(i)
            adjs = graph[i]
            for adj in adjs:
                if adj not in visited:
                    stack.append(adj)

        return n - 1 == len(edges) and len(visited) == n
        
