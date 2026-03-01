class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        
        print(nums[pivot])
        if pivot >= 0:
            succ = len(nums) - 1
            while nums[succ] <= nums[pivot]:
                succ -= 1
            nums[succ], nums[pivot] = nums[pivot], nums[succ]
        
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
