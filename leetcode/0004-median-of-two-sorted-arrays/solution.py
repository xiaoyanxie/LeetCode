class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def bsearch(n, nums, assist):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                elementsMin = mid + bisect.bisect_left(assist, nums[mid])
                elementsMax = mid + bisect.bisect_right(assist, nums[mid])
                if elementsMin <= n <= elementsMax:
                    return nums[mid]
                elif elementsMax < n:
                    l = mid + 1
                else:
                    r = mid - 1
            # print('Not found')
            return None

        def find(n):
            med = bsearch(n, nums1, nums2)
            if med is not None:
                return med
            return bsearch(n, nums2, nums1)

        size = len(nums1) + len(nums2)
        if size % 2 == 0:
            N = (size - 2) / 2
            a = find(N)
            b = find(N + 1)
            return (a + b) / 2
        else:
            N = (size - 1) / 2
            return find(N)
