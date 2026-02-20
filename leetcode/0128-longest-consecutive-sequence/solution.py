class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0

        for num in numSet:
            if num-1 not in numSet:
                curr = num
                count = 1

                while (curr + 1) in numSet:
                    count += 1
                    curr += 1
                
                maxCount = max(count, maxCount)
        
        return maxCount


            
