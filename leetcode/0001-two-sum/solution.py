from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i, n in enumerate(nums):
            peer = target - n
            if peer in seen:
                return [seen[peer], i]
            else:
                seen[n] = i
        return []
