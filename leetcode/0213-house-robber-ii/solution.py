class Solution:
    def rob(self, nums: List[int]) -> int:
        #subproblem: dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        #circle: 1. range(1, len(nums)) 2. range(2, len(nums) + 1)
        #base case: dp[1] = 1 
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * (len(nums) + 1)

        dp[0] = 0 
        dp[1] = nums[0]

        # get rid of the last house
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        tmp = dp[len(nums) - 1]

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = nums[1]
        #get rid of the first house
        for i in range(3, len(nums) + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return max(tmp,dp[len(nums)])
