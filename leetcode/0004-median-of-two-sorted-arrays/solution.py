class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1,  3,     5,   8, 10, 12
        l1
                           r1
          2,  4, 5,   6,     11
          l2                 r2

        1 2 3 4
        5 6 7 8

        1 2 3 4
                l   
              r
        5 6 7 8 9 10
          l
          r
        
        1 2 3
            l   
            r
        4 5

        if #elements <- median == length // 2:
            return median if length is even, or return (median1 + median2) / 2
        elif #elements <- median < length // 2:
            l = mid + 1
        else:
            r = mid - 1

        1, 3
           l  
           r
        2, 7

        2, 2, 4, 4
        l   
                 r
        2, 2, 4, 4
        """
        length = len(nums1) + len(nums2)

        def searchMedian(arr, assist, expectedSize) -> Optional[int]:
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                # expectedSize = length // 2 # 4
                lo = bisect.bisect_left(assist, arr[mid])
                hi = bisect.bisect_right(assist, arr[mid])
                sizeLo = lo + mid
                sizeHi = hi + mid
                if sizeLo <= expectedSize <= sizeHi:
                    return arr[mid]
                elif expectedSize < sizeLo:
                    r = mid - 1
                else:
                    l = mid + 1
            return None


        # 1,2,3,4,5
        mid = searchMedian(nums1, nums2, length // 2)
        if mid == None:
            mid = searchMedian(nums2, nums1, length // 2)
        assert mid != None
        if length % 2 != 0:
            return mid

        mid1 = searchMedian(nums1, nums2, length // 2 - 1)
        if mid1 == None:
            mid1 = searchMedian(nums2, nums1, length // 2 - 1)
        assert mid1 != None
        return (mid + mid1) / 2
