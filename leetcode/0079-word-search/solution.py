class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        ABCCED
             ^
        """
        # visited = set()
        self.dire = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(idx, i, j):
            if board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            
            
            # visited.add((i,j))
            board[i][j] = "#"
            
            for a,b in self.dire:
                nx, ny = i + a, j + b
                if 0 <= nx < m and 0 <= ny < n:
                    if dfs(idx + 1, nx, ny):
                        return True 
            board[i][j] = word[idx]
            return False

        m = len(board)
        n = len(board[0])
        #pruning
        table = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                table[board[i][j]] += 1

        wordCount = collections.Counter(word)
        for key in wordCount.keys():
            if wordCount[key] > table[key]:
                return False
        #pruning ends
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True
        
        return False
