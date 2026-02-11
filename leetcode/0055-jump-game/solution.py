class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        [2,3,1,1,4]
           ^
        longest = 4
        steps = 1


        [3,2,1,0,4]
               ^
        longest = 3
        steps = 4

        [2,4,2,1,1,1,0,1] 7
                i
        longest = 6
        steps = 6
        """

        longest = 0
        steps = 0
        for i, s in enumerate(nums):
            if i > longest:
                return False
            longest = max(longest, steps + s)
            steps += 1
            # print(f'{longest}, {steps}')
            if longest >= len(nums) - 1:
                return True
        return True

