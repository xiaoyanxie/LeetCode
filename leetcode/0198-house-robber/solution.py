class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i, n in enumerate(nums):
            if i == 0: continue
            j = i + 1
            dp[j] = max(nums[i] + dp[j - 2], dp[j - 1])

        return dp[-1]
