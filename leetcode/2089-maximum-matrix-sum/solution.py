class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        [ 1, 2, 3],
        [-1, 2, 3],
        [ 1, 2, 3]

        if there there are odd negatives numbers:
            sum of all abs(n) - 2 * abs(min)
        elif:
            sum of all abs(n)
        """

        n = len(matrix)

        # 1. count the negatives
        negatives = 0
        total = 0
        minimum = inf
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negatives += 1
                total += abs(matrix[i][j])
                minimum = min(minimum, abs(matrix[i][j]))
        
        # 2. calculate
        if negatives % 2 != 0:
            return total - 2 * minimum
        else:
            return total
