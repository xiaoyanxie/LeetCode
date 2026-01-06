class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        visited = set()
        def dfs(graph, root) -> int:
            if not graph[root]:
                return 0
            visited.add(root)
            # height = []
            top1 = 0
            top2 = 0
            for adj in graph[root]:
                if adj in visited:
                    continue
                hei = 1 + dfs(graph, adj)
                if hei > top1:
                    top2 = top1
                    top1 = hei
                elif hei > top2:
                    top2 = hei
                # height.append(hei)
            
            # if not height:
            #     return 0
            self.maxLen = max(self.maxLen, top1+top2)
            # height.sort()
            # if len(height) == 1:
            #     self.maxLen = max(self.maxLen, height[-1])
            # elif len(height) > 1:
            #     self.maxLen = max(self.maxLen, height[-1] + height[-2])
            
            return top1

        if not edges:
            return 0
        graph = {}
        for edge in edges:
            if edge[0] not in graph.keys():
                graph[edge[0]] = list()
            if edge[1] not in graph.keys():
                graph[edge[1]] = list()
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        self.maxLen = 0
        
        dfs(graph, edges[0][0])
        return self.maxLen
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # edges.sort()
        # if not edges or not edges[0]:
        #     return 0

        # #O(E)
        # hmap = {}
        # for edge in edges:
        #     if edge[0] not in hmap.keys():
        #         hmap[edge[0]] = list()
        #     if edge[1] not in hmap.keys():
        #         hmap[edge[1]] = list()
        #     hmap[edge[0]].append(edge[1])
        #     hmap[edge[1]].append(edge[0])
      
        # visited = set()
        # def dfs(graph, root) -> int:
        #     visited.add(root)
        #     if not graph[root]:
        #         return 0
        #     heights = []
        #     for adj in graph[root]:
        #         if adj in visited:
        #             continue
        #         height = 1 + dfs(graph, adj)
        #         heights.append(height)
            
        #     if not heights:
        #         return 0
            
        #     heights.sort()
        #     if len(heights) == 1:
        #         self.maxD = max(self.maxD, heights[-1])
        #     else:
        #         self.maxD = max(self.maxD, heights[-1] + heights[-2])
        #     return max(heights)

        # self.maxD = 0
        # dfs(hmap, edges[0][0])
        # return self.maxD
        

