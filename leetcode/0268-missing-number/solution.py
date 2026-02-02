class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        n = len(nums)
        expected_sum = int((n * (n + 1)) / 2)
        return expected_sum - actual_sum
