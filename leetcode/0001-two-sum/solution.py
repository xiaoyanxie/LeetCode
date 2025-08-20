class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in map:
                return [map[remain], i]
            else:
                map[num] = i
        
        return []

