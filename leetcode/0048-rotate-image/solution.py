class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #flip left and right
        n = len(matrix)
        for i in range(n):
            for j in range(0, n//2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
        #flip top left and bottom right
        for i in range(n):
            for j in range(0, n - i - 1):
                matrix[i][j],matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1],matrix[i][j]

        return matrix
    
