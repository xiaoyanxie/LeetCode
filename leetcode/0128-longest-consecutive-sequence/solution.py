class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # lookup: ()
        # len = 1
        # maxLen = 4
        # [100,4,200,1,3,2]
        #                 ^
        lookup = set(nums)
        maxLen = 0
        for n in nums:
            length = 0
            # explore left
            i = n
            while i in lookup:
                length += 1
                lookup.remove(i)
                i -= 1
            # explore right
            j = n + 1
            while j in lookup:
                length += 1
                lookup.remove(j)
                j += 1
            if length > maxLen:
                maxLen = length
        
        return maxLen
