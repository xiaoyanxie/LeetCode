class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        if nums[l] < nums[r]:
            return nums[l]
        if n <= 2:
            return min(nums)

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid

        return nums[mid]
