class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        def side(num):
            if num > nums[-1]:
                return 'left'
            else:
                return 'right'

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if side(nums[mid]) == side(target):
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
