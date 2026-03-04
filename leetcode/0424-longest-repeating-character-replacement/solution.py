class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count = collections.Counter()
        # if len(s) == 1:
        #     return 1
        # l = 0
        # r = 0
        # maxCnt = 0
        # maxWin = 0

        # for r in range(len(s)):
        #     count[s[r]] += 1
            
        #     maxCnt = max(maxCnt, count[s[r]])
        #     if r - l + 1 - maxCnt > k:
        #             count[s[l]] -= 1
        #             l += 1
        #     maxWin = max(maxWin, r - l + 1)
        # return maxWin
        count = [0] * 26
        # for i in range(len(s)):
        #     idx = ord(s[i]) - ord('A')
        #     count[idx] += 1
        
        maxCnt = 0
        maxWin = 0
        l = r = 0
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            maxCnt = max(maxCnt, count[idx])
            if r - l + 1 - maxCnt > k:
                lidx = ord(s[l]) - ord('A')
                count[lidx] -= 1
                l +=1
            maxWin = max(maxWin, r - l + 1)
        return maxWin


