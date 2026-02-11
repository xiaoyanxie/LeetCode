class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Paths[i][j] = Paths[i - 1][j] + Paths[i][j - 1]
        Paths[0][0] = 1

        1,1,1,1,1,1,1
        1,2,3,4,5,6,7
        1,3,6,10,15,21,28

        """

        paths = [ [0] * n for _ in range(m) ]
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = paths[i - 1][j] if i > 0 else 0
                left = paths[i][j - 1] if j > 0 else 0
                paths[i][j] =  top + left

        return paths[m - 1][n - 1]
