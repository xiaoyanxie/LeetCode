class Solution:

    # abbabcba
    #   i
    #     j
    def expand(self, s, i, j) -> int:
        n = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            length = j - i + 1
            n += 1
            i -= 1
            j += 1
        return n
    
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i, c in enumerate(s):
            count += self.expand(s, i, i)
            if i > 0:
                count += self.expand(s, i - 1, i)

        return count
