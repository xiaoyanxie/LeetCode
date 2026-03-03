from collections import deque
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
           2
          3 4
         6 5 7
        4 1 8 3

          2
        5.  6
      11  10.   11
    15  11.  18    14
        
        2, 0 -> 12
        2, 1 -> 11
        1, 0 -> 11
        """

        pathSums = [ [0] * len(row) for row in triangle ]

        for i, row in enumerate(triangle):
            for j, num in enumerate(row):
                # min of the pathSum of num
                if i == 0:
                    pathSums[i][j] = num
                    continue
                if 0 < j < len(row) - 1:
                    pathSums[i][j] = num + min(pathSums[i - 1][j], pathSums[i - 1][j - 1])
                elif j == 0:
                    pathSums[i][j] = num + pathSums[i - 1][j]
                else:
                    pathSums[i][j] = num + pathSums[i - 1][j - 1]

        return min(pathSums[-1])

        # BFS
        # queue = deque([(0, 0, 0)])
        # best = inf
        # while queue:
        #     i, j, pathSum = queue.popleft()
        #     if i == len(triangle):
        #         best = min(pathSum, best)
        #         continue
        #     queue.append((i + 1, j, pathSum + triangle[i][j]))
        #     queue.append((i + 1, j + 1, pathSum + triangle[i][j]))
        # return best
        # @cache
        # def dfs(i, j, pathSum): # 1, 0, 11
        #     if i == len(triangle):
        #         return pathSum
        #     pathSum += triangle[i][j] # 15
        #     sum1 = dfs(i + 1, j, pathSum)
        #     sum2 = dfs(i + 1, j + 1, pathSum)
        #     return min(sum1, sum2)

        # return dfs(0, 0, 0)
