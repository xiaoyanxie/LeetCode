class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        dp = [0] *(len(nums))
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        max1 = dp[-1]
        print(max1)
        dp = [0] *(len(nums))
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
        return max(max1, dp[-1])
