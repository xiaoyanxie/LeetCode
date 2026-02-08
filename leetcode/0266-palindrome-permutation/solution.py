class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #palindrome: 0 or 1 odd letter
        # numOdd = 0
        # table = {}
        # for letter in s:
        #     if letter in table:
        #         table[letter] += 1
        #         if table[letter] % 2 == 0:
        #             numOdd -= 1
        #         else:
        #             numOdd += 1
        #     else:
        #         table[letter] = 1
        #         numOdd += 1
        
        # return numOdd <=1
        odd = set()
        for i in s:
            if i in odd:
                odd.remove(i)
            else:
                odd.add(i)
        return len(odd) <= 1
