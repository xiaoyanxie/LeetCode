class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [ [0] * (row + 1) for row in range(query_row + 1) ]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(row + 1):
                if tower[row][glass] < 1:
                    continue
                
                extra = (tower[row][glass] - 1) / 2
                tower[row + 1][glass] += extra
                if glass + 1 <= row + 1:
                    tower[row + 1][glass + 1] = extra
        
        # print(tower)

        if tower[query_row][query_glass] > 1:
            return 1
        
        return tower[query_row][query_glass]
