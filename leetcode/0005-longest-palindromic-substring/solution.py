class Solution:
    def longestPalindrome(self, s: str) -> str:
        # abaabba

        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return (i + 1, j)

        best = ""
        for i in range(len(s)):
            print(f"search from s[{i}] = {s[i]}")
            start, end = expand(i, i)
            print(f"found {s[start:end]}")
            if end - start > len(best):
                best = s[start:end]
            if i + 1 == len(s):
                continue

            print(f"search from s[{i}] = {s[i]} and s[{i + 1}] = {s[i + 1]}")
            start1, end1 = expand(i, i + 1)
            print(f"found {s[start1:end1]}")
            if end1 - start1 > len(best):
                best = s[start1:end1]
        
        return best
