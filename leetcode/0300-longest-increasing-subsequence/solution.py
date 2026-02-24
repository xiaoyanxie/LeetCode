class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for i in range(1, len(nums)):
            j = bisect.bisect_left(sub, nums[i])
            if j == len(sub):
                sub.append(nums[i])
            else:
                sub[j] = nums[i]
        return len(sub)
