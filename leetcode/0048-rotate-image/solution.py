class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # #flip upside down
        # n = len(matrix)
        # for i in range(n//2):
        #     for j in range(n):
        #         matrix[i][j], matrix[n - i - 1][j]= matrix[n - i - 1][j],matrix[i][j]

        # # flip across 
        # for i in range(n):
        #     for j in range(i+1, n):
        #         matrix[i][j], matrix[j][i] = matrix [j][i], matrix[i][j]    
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

        # return matrix
