class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_side(n):
            if nums[0] > n <= nums[-1]:
                return 'right'
            else:
                return 'left'
            
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if get_side(nums[mid]) == get_side(target):
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
