class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #subproblem: max subarray ending with index i dp[i]
        #base case: dp[0]
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
        
        return max(dp)

