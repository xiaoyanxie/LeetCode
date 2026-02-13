class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vertical = [ (1, 0), (-1, 0) ]
        horizontal = [ (0, 1), (0, -1) ]

        rows = len(matrix)
        cols = len(matrix[0])

        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def allZeros(i, j, directions):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if isValidLoc(ni, nj) and matrix[ni][nj] != 0:
                    return False
            return True

        def markZeros(i, j, directions):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                while isValidLoc(ni, nj):
                    if matrix[ni][nj] != 0:
                        matrix[ni][nj] = -inf
                    ni, nj = ni + di, nj + dj
    
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0: continue
            
                if not allZeros(i, j, vertical):
                    markZeros(i, j, vertical)
                if not allZeros(i, j, horizontal):
                    markZeros(i, j, horizontal)
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -inf:
                    matrix[i][j] = 0
