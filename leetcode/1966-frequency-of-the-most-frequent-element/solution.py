class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        1,4,4,5,8,13
                l
                   r

        ops: 5
        maxFreq: 3

        inc r: ops += (nums[r] - nums[r - 1]) * (r - l)

        inc l: ops -= (nums[r - 1] - nums[l])
        """
        if len(nums) == 1:
            return 1

        nums.sort()
        l = 0
        ops = 0
        maxFreq = 0
        for r in range(1, len(nums)):
            ops += (nums[r] - nums[r - 1]) * (r - l)
            while ops > k:
                ops -= (nums[r] - nums[l])
                l += 1
            maxFreq = max(maxFreq, r - l + 1)
        
        return maxFreq
