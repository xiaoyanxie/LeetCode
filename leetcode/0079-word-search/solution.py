class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        dfs(i, j, k, visited)    
        
        ABCCED
            k

        dfs(0, 0, 0, {A}) -> dfs(1, 0, 1, {A, S}) -> False
                          -> dfs(0, 1, 1, {A, B}) -> dfs(0, 2, 2, {A, B, C}) -> dfs(0, 3, 3, {A, B, C, E}) -> False
                                                                             -> dfs(1, 2, 3, {A, B, C, C}) -> ... -> dfs(2, 1, 5, {A, B, C, C, E, D}) -> True
        """
        rows = len(board)
        cols = len(board[0])

        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        def isValidLoc(i, j) -> bool:
            return 0 <= i < rows and 0 <= j < cols

        def dfs(i, j, k) -> bool: # k=5, i=2, j=1
            # base case:
            if k == len(word) - 1:
                return True
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if not isValidLoc(ni, nj) or board[ni][nj] == '' or board[ni][nj] != word[k + 1]:
                    continue
                
                char = board[ni][nj]
                board[ni][nj] = ''

                if dfs(ni, nj, k + 1):
                    board[ni][nj] = char
                    return True
                board[ni][nj] = char
            
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    board[i][j] = ''
                    if dfs(i, j, 0):
                        board[i][j] = word[0]
                        return True
                    board[i][j] = word[0]
        
        return False
