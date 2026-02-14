class Solution:
    def rotatedDigits(self, n: int) -> int:
        #rotatable and good, another digit: 2, 5, 6, 9
        #valid: rotatable but not good, themselves: 0, 1, 8
        # invalid, not rotatable: 3, 4, 7
        #856
        #dp = [2, 2, 0]
        good = {2, 5, 6, 9}
        bad = {3, 4, 7}
        cnt = 0
        dp = [2] * (n + 1)
        for i in range(0, min(10, n + 1)):
            if i in good:
                dp[i] = 0
            elif i in bad:
                dp[i] = 1
           
        for i in range(1, n + 1):
            digit = i // 10
            remain = i % 10
            if dp[digit] == 1 or dp[remain] == 1:
                dp[i] = 1
                continue
            if dp[digit] == 0 or dp[remain] == 0:
                dp[i] = 0
                cnt += 1
        return cnt
                
        # for i in range(1, n+1):
        #     hasBad = False
        #     hasGood = False
        #     # container = set()
        #     tmp = i
        #     while tmp > 0:    
        #         digit = tmp % 10
        #         if digit in bad:
        #             hasBad = True
        #             break
        #         elif digit in good:
        #             hasGood = True
        #         tmp = tmp // 10

        #     # if not (container & bad) and (good & container):
        #     if not hasBad and hasGood:
        #         cnt += 1
            
        # return cnt
