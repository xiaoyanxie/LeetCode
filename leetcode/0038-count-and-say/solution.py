class Solution:
    def countAndSay(self, n: int) -> str:
        """
        1 -> 11 -> 21 -> 1211 -> 111221 -> 312211 -> 13112221

        Time: O(N^2)
        Space: O(N)
        """
        # def rle(n): # 4
        #     if n == 1:
        #         return '1'
        #     s = rle(n - 1)
            
        #     stack = [] # [1, 1], [2, 1], [1, 2] 
        #     for c in s:
        #         if stack and c == stack[-1][0]:
        #             stack[-1][1] += 1
        #         else:
        #             stack.append([c, 1])
        #     # print(stack)
        #     rleStr = ''.join( f'{cnt}{c}' for c, cnt in stack) # 1211
        #     # print(f'rle({n}) = RLE of {s} = {rleStr}')
        #     return rleStr

        # return rle(n)

        rle = '1'
        for _ in range(2, n + 1):
            stack = [] # [1, 1], [2, 1], [1, 2] 
            for c in rle:
                if stack and c == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([c, 1])
            rle = ''.join( f'{cnt}{c}' for c, cnt in stack) # 1211

        return rle
