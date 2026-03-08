from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        0123456789
        loveleetcode
                   ^

        freq: {
            l: [0, 2],
            o: [1, 2],
            v: [2, 1], <-
            e: [3, 4],
            t: [7, 1], <-
            c: [8, 1], <-
            d: [10, 1] <-
        }
        """
        freq = {}
        for i, c in enumerate(s):
            if c not in freq:
                freq[c] = [i, 1]
            else:
                freq[c][1] += 1
        
        first = inf # 2
        for c in freq:
            if freq[c][1] == 1 and freq[c][0] < first:
                first = freq[c][0]
        
        return first if first != inf else -1
