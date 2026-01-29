# class Iter:
#     def __init__(self, nums1, nums2):
#         self.nums1 = nums1
#         self.nums2 = nums2
    
#     def has_next():
#         self.i < len(self.nums1) + len(self.nums2)

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        
        # Helper to find the k-th smallest element (1-based index)
        def findKth(k, a_start, a_end, b_start, b_end):
            # If a segment is empty, return the k-th from the other
            if a_start > a_end: return nums2[b_start + k - 1]
            if b_start > b_end: return nums1[a_start + k - 1]
            
            # Base case: if k is 1, return the min of the starts
            if k == 1: return min(nums1[a_start], nums2[b_start])
            
            # Get middle elements to compare (use inf if out of bounds)
            mid_a = nums1[a_start + k//2 - 1] if a_start + k//2 - 1 <= a_end else float('inf')
            mid_b = nums2[b_start + k//2 - 1] if b_start + k//2 - 1 <= b_end else float('inf')
            
            # Discard the smaller half
            if mid_a < mid_b:
                return findKth(k - k//2, a_start + k//2, a_end, b_start, b_end)
            else:
                return findKth(k - k//2, a_start, a_end, b_start + k//2, b_end)

        # Logic for odd vs even total length

        # nums1 = [1,2,5,8,11], nums2 = [3,6,7,9,10]

        # 0, 1, 2, 3, 5, 6, 7, 8, 9, 10

        if total % 2 == 1:
            return findKth(total // 2 + 1, 0, m-1, 0, n-1)
        else:
            return (findKth(total // 2, 0, m-1, 0, n-1) + 
                    findKth(total // 2 + 1, 0, m-1, 0, n-1)) / 2.0
