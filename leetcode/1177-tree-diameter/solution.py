class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # edges.sort()
        if not edges or not edges[0]:
            return 0

        #O(E)
        hmap = {}
        for edge in edges:
            if edge[0] not in hmap.keys():
                hmap[edge[0]] = list()
            if edge[1] not in hmap.keys():
                hmap[edge[1]] = list()
            hmap[edge[0]].append(edge[1])
            hmap[edge[1]].append(edge[0])
      
        visited = set()
        self.maxD = 0
        def dfs(graph, root) -> int:
            visited.add(root)
            if not graph[root]:
                return 0
            heights = []
            for adj in graph[root]:
                if adj in visited:
                    continue
                height = 1 + dfs(graph, adj)
                heights.append(height)
            
            if not heights:
                return 0
            
            heights.sort()
            if len(heights) == 1:
                self.maxD = max(self.maxD, heights[-1])
            else:
                self.maxD = max(self.maxD, heights[-1] + heights[-2])
            return max(heights)

        dfs(hmap, edges[0][0])
        return self.maxD
        # top1 =0
        # top2 = 0
        # for value in hmap.values():
        #     length = len(value)
        #     if length > top1:
        #         top2 = top1
        #         top1 = value
        #     if length > top2:
        #         top2 = value
        # return top1+top2

