class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        #.             right,  down,    left.    up
        currentDirection = 0
        rowsLo = 0
        rowsHi = len(matrix)
        colsLo = 0
        colsHi = len(matrix[0])

        def nextDirection():
            nonlocal currentDirection, rowsLo, rowsHi, colsLo, colsHi

            if currentDirection == 0:
                rowsLo += 1
            elif currentDirection == 1:
                colsHi -= 1
            elif currentDirection == 2:
                rowsHi -= 1
            else:
                colsLo += 1

            currentDirection = (currentDirection + 1) % 4

        loc = (0, 0)

        def isValidLoc(di, dj):
            return rowsLo <= loc[0] + di < rowsHi and colsLo <= loc[1] + dj < colsHi
        def nextLoc():
            nonlocal loc
            di, dj = directions[currentDirection]
            if isValidLoc(di, dj):
                loc = (loc[0] + di, loc[1] + dj)
                return True
            nextDirection()

            di, dj = directions[currentDirection]
            if isValidLoc(di, dj):
                loc = (loc[0] + di, loc[1] + dj)
                return True
            return False

        result = []
        while True:
            result.append(matrix[loc[0]][loc[1]])
            if not nextLoc():
                break
        return result
