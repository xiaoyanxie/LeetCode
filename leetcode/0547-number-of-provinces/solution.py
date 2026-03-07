from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
           0 1 2
        0 [1,1,0],
        1 [1,1,0],
        2 [0,0,1]

        (1, 2), (2, 1)

        provinces = n
        for all edges from i -> j, call union(i, j):
            if they share the same parent:
                provinces -= 1
        """

        provinces = len(isConnected) # 2

        uf = [i for i in range(provinces)] # [1,1,2]
        def find(i):
            if uf[i] == i:
                return i
            uf[i] = find(uf[i])
            return uf[i]
        
        def union(i, j):
            nonlocal provinces
            p1 = find(i)
            p2 = find(j)

            if p1 != p2:
                uf[p1] = p2
                provinces -= 1
        
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        return provinces
