class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i = len(word1)
        j = len(word2)
        if not word1:
            return j
        if not word2:
            return i

        mem = [[0] * (j + 1) for _ in range(i + 1)]
        for a in range(i+1):
            mem[a][0] = a
        for b in range(j+1):
            mem[0][b] = b
        
        for a in range(1,i+1):
            for b in range(1,j+1):
                if word1[a-1] == word2[b-1]:
                    mem[a][b] = mem[a-1][b-1]

                else:
                    mem[a][b] = 1 + min(mem[a][b-1], mem[a-1][b], mem[a-1][b-1])
        

        return mem[i][j]
