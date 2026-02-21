import heapq

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        [ 1, 2, 3],
        [-1,-2,-3],
        [ 1, 2, 3]

        [-1, 0,-1],
        [-2, 1, 3],
        [ 3, 2, 2]

        [ 2, 9, 3],
        [ 5, 4,-4],
        [ 1, 7, 1]

        gain = (totalSum - num1 - num2 - num1 - num2) - totalSum
        
        even # of negatives: they can all be cancelled out
        odd # of negatives: leave the largest negative number
        """

        rows = len(matrix)
        cols = len(matrix[0])
        
        total = 0
        negatives = 0
        minabs = inf
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] <= 0:
                    negatives += 1
                if minabs > abs(matrix[i][j]):
                    minabs = abs(matrix[i][j])
                total += abs(matrix[i][j])
        
        # print(minabs)
        if negatives % 2 == 0:
            return total
        else:
            return total - 2*minabs
        # 
        # 
        # 

        # totalSum = 0
        # for i in range(rows):
        #     for j in range(cols):
        #         totalSum += matrix[i][j]

        # def gain(i, j, di, dj):
        #     ni, nj = i + di, j + dj
        #     if not isValidLoc(ni, nj):
        #         return -1
            
        #     num1, num2 = matrix[i][j], matrix[ni][nj]
        #     new = totalSum - 2*num1 - 2*num2
        #     return new - totalSum
        
        # maxheap = []
        # for i in range(rows):
        #     for j in range(cols):
        #         for di, dj in directions:
        #             g = gain(i, j, di, dj)
        #             if g < 0: continue
        #             heapq.heappush(maxheap, ( -g, i, j, di, dj ))
        
        # # while 
