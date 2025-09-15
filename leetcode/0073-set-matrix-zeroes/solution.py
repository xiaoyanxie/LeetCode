class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #for each cell, find 0 and check if the row/colum is 0, if not replace
        zeroCol = set()
        zeroRow = set()
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeroRow.add(i)
                    zeroCol.add(j)
        

        for i in range(row):
            if i in zeroRow:
                for j in range(col):
                    matrix[i][j] = 0
                    
        for j in range(col):
            if j in zeroCol:
                for i in range(row):
                    matrix[i][j] = 0     


