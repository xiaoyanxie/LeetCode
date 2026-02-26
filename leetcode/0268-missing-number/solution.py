class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     if nums[0] == 0:
        #         return 1
        #     else:
        #         return 0

        # nums.sort()
        # if nums[0] != 0:
        #     return 0
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i - 1] != 1:
        #         return i
        
        # return len(nums)
        target = (0 + len(nums)) * (len(nums) + 1) // 2
    
        for num in nums:
            target -= num
        return target


