class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, a in enumerate(nums):
            b = target - a
            if b in seen:
                return [seen[b], i]
            else:
                seen[a] = i
        return [-1, -1]
