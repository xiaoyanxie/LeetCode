class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        l,r = 0, length - 1

        if length == 1:
            return nums[0]

        if nums[0] <= nums[length - 1]:
            return nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid+1]
            elif nums[l] < nums[mid]:
                l = mid
            else:
                r = mid
        
        return -1
