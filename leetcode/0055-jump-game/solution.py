class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [2,3,1,1,4]
        #. 2 4 3 4 0

        # [3,2,1,0,4]
        #  3 3 3 3  

        far = 0
        for i, step in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + step)
            if far >= len(nums) - 1:
                return True
        return far >= len(nums) - 1
