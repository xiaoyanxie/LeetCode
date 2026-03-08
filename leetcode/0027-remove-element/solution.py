class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        3,3,2,3
            i
               j
        
        0,1,2,2,3,0,4,2
            l
                r
        """
        l = 0
        while l < len(nums) and nums[l] != val:
            l += 1

        for r in range(l + 1, len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return l
