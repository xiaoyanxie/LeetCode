class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, num in enumerate(nums):
            if target - num not in seen:
                seen[num] = i
            else:
                return [i, seen[target-num]]
        
