class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        end = 0
        steps = 0
        for i, s in enumerate(nums):
            if i == len(nums) - 1:
                break
            far = max(far, i + s)
            if i == end:
                steps = steps + 1
                end = far
        return steps
            
