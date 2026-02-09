class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        [1,2,3],
        [4,5,6],
        [7,8,9]

        [3,2,1],
        [6,5,4],
        [9,8,7]

        [7,4,1],
        [8,5,2],
        [9,6,3]

        (0, 2) - (0, 2)
        (0, 1) - (1, 2)
        (0, 0) - (2, 2)
        """
        N = len(matrix)

        for i in range(len(matrix)):
            a, b = 0, len(matrix[0]) - 1
            while a < b:
                matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
                a += 1
                b -= 1
        
        for i in range(N):
            for j in range(N - i - 1):
                a, b = N - 1 - j, N - 1 - i
                matrix[i][j], matrix[a][b] = matrix[a][b], matrix[i][j]

