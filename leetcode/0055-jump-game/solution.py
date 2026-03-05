class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        maxReach = nums[0]
        for i, num in enumerate(nums):
            if i > maxReach:
                return False
            if num + i > maxReach:
                maxReach = num + i
            if maxReach >= len(nums) - 1:
                return True
        
        return True

# last:3
# i:3

        # dp = [False] * (len(nums))
        # dp[0] = True
        # for i in range(1, len(nums)):
        #     for j in range(0, i):
        #         if dp[j] == True and i - j <= nums[j]:
        #             dp[i] = True
        #             break
        #     if dp[i] == False:
        #         return False
        
        # return dp[len(nums)-1]
        
