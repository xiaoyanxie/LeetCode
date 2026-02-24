class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AABABBA
        l
         r
        """
        freq = defaultdict(int)
        l = 0
        best = 0
        maxfreq = 0
        for r, c in enumerate(s):
            freq[c] += 1
            maxfreq = max(freq[c], maxfreq)
            while (r - l + 1) - maxfreq > k:
                freq[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
