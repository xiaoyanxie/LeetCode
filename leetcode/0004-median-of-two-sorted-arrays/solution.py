class Solution:
    def merge(self, nums1, nums2) -> List[int]:
        N = len(nums1) + len(nums2)
        merged = [None] * N
        i = 0
        j = 0
        k = 0
        while j < len(nums1) or k < len(nums2):
            if j < len(nums1) and k < len(nums2):
                if nums1[j] < nums2[k]:
                    merged[i] = nums1[j]
                    j += 1
                else:
                    merged[i] = nums2[k]
                    k += 1
            elif j < len(nums1):
                merged[i] = nums1[j]
                j += 1
            else:
                merged[i] = nums2[k]
                k += 1
            i += 1
        return merged
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.merge(nums1, nums2)
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[mid] + nums[mid - 1]) / 2.0
        else:
            return nums[mid]
