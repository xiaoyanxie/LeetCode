class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
         zeros: 2
         ones: 0
         total: 1

 ones    0     0     1    2   2   2    1   2
 zeros   1     2     2    2   1   2    2   2
        "0     0     1    1   0   0    1   1"
                                           ^
                     1    1   1   1    1   1
 ones.  1 1 1 1 1
 zeros  0 1 1 1 1 
        1 0 1 0 1
          1 1 1 1

 ones   0 1
 zeros  1 1
        0 1
          1
        """

        """
     1s  00122200
     0s  12221200
        "00110011"
               ^
         total = 4

   prev  00222222
   curr  12121212
        "00110011"
         
        """
        prev = 0
        curr = 1
        total = 0

        for i, c in enumerate(s):
            if i == 0: 
                continue
            if s[i - 1] == c: # grouped
                curr += 1
            else:
                prev = curr
                curr = 1
            
            if prev >= curr:
                total += 1
        return total
