class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        

        4,1,2,1,2
        
        """
        test = 0
        for n in nums:
            test ^= n
        return test
