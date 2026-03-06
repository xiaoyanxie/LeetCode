class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # def flip(m,n):
        #     for i in range(len(matrix[0])):
        #         if matrix[m][i] != 0:
        #             matrix[m][i] = 'z'
        #     for j in range(len(matrix)):
        #         if matrix[j][n] != 0:
        #             matrix[j][n] = 'z'

        # for m in range(len(matrix)):
        #     for n in range(len(matrix[0])):
        #         if matrix[m][n] == 0:
        #             flip(m, n)

        # for m in range(len(matrix)):
        #     for n in range(len(matrix[0])):
        #         if matrix[m][n] == 'z':
        #             matrix[m][n] = 0
        
        # return matrix
        r = len(matrix)
        c = len(matrix[0])
        isRow = False
        isCol = False
        for i in range(c):
            if matrix[0][i] == 0:
                isRow = True
        for j in range(r):
            if matrix[j][0] == 0:
                isCol = True

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, c):
            if matrix[0][i] == 0:
                for j in range(r):
                    matrix[j][i] = 0
        for i in range(1, r):
            if matrix[i][0] == 0:
                for j in range(c):
                    matrix[i][j] = 0
        if isRow:
            for i in range(c):
                matrix[0][i] = 0
        if isCol:
            for j in range(r):
                matrix[j][0] = 0
        return matrix 

        
