class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        ABCCED
             ^
        """
        visited = set()
        self.dire = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(idx, i, j):
            
            if board[i][j] != word[idx]:
                return False
            visited.add((i,j))
            
            if board[i][j] == word[idx] and idx == len(word) - 1:
                return True

            for a,b in self.dire:
                nx, ny = i + a, j + b
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if dfs(idx + 1, nx, ny):
                        return True 
            visited.remove((i,j))
            return False

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and (i,j) not in visited:
                    if dfs(0, i, j):
                        return True
        
        return False
