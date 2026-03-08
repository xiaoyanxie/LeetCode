class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        """
        541

        5! + 4! + 1! = 145
        """
        s = str(n)
        factSum = str(sum( math.factorial(int(i)) for i in s ))
        return Counter(s) == Counter(factSum)
