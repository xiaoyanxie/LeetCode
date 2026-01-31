class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [100,4,200,1,3,2]
        # { 4:0, 1:0, 3:0, 2:0 }

        # [101,4,100,102,1,3,2]
        #                     ^

        lookup = set(nums) # {101,4,100,102,1,3,2}
        visited = set() # {101, 102, 100, 4, 3, 2, 1}
        maxLen = 0 # 4

        for n in nums:  # 4
            if n in visited:
                continue
            length = 0 # 4
            i = n # 4
            while i in lookup: # 5
                length += 1
                visited.add(i)
                i += 1

            j = n - 1
            while j in lookup: # 1
                length += 1
                visited.add(j)
                j -= 1
                
            if length > maxLen:
                maxLen = length

        return maxLen
