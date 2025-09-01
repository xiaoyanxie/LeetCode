class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = col
        top = 0
        bott = row
        res = []
        length = row * col
       
        while l < r and top < bott:
            for i in range(l, r):
                res.append(matrix[top][i])
            #update top bound
            top += 1
            for i in range(top, bott):
                res.append(matrix[i][r - 1])
            #update right bound
            r -= 1
            if not(l < r and top < bott):
                return res

            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bott - 1][i])
            #update bott bound
            bott -= 1

            for i in range(bott - 1, top - 1, -1):
                res.append(matrix[i][l])
            #udpate left bound
            l += 1



        return res
        

