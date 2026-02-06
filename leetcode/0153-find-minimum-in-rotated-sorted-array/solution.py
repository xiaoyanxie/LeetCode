class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 4,5,6,7,0,1,2
        # 0,1,2
        # i m j
        # 2,1,0
        # i   j
        # [1]
        # ij
        def left(i):
            if i > 0:
                return nums[i - 1]
            else:
                return nums[-1]

        def right(i):
            return nums[(i + 1) % len(nums)]

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2

            if left(mid) >= nums[mid] <= right(mid):
                return nums[mid]
            if nums[mid] > nums[-1]:
                i = mid + 1
            else:
                j = mid - 1

        return -1
