class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        
        last = nums[0]
        maxsum = nums[0]
        for num in nums[1:]:
                cur = max(last + num, num)
                maxsum = max(maxsum, cur)
                last = cur
        
        return maxsum


