class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Node()
        
        # init trie
        for word in words:
            curr = trie
            for i, c in enumerate(word):
                if c in curr.children:
                    curr = curr.children[c]
                    continue
                curr.children[c] = Node()
                curr = curr.children[c]
            curr.isWord = True
            curr.word = word

        # search through the board
        rows = len(board)
        cols = len(board[0])

        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols
        
        def search(board, i, j, children, ret):
            if board[i][j] not in children:
                return
            
            node = children[board[i][j]]
            if node.isWord:
                ret.append(node.word)
                node.isWord = False
            
            for di, dj in [ (0, 1), (0, -1), (1, 0), (-1, 0) ]:
                ni, nj = i + di, j + dj
                if not isValidLoc(ni, nj) or board[ni][nj] == '':
                    continue
                tmp, board[i][j] = board[i][j], ''
                search(board, ni, nj, node.children, ret)
                board[i][j] = tmp

        ret = []
        for i in range(rows):
            for j in range(cols):
                search(board, i, j, trie.children, ret)

        return ret
