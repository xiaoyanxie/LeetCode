class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob(houses):
            prev2, prev1 = 0, 0
            for val in houses:
                amt = max(prev1, val + prev2)
                prev2 = prev1
                prev1 = amt
            return prev1

        return max(rob(nums[1:]), rob(nums[0:-1]))
