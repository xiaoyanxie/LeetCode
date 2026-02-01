class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #sums1 = 4, sums2 = 5 nums with 0 bigger than the other by 1*# zeros or more
        #sums1, sums2, #zeros in nums1, nums2
        
        #1. check the number of zeros and get sums
        #2. if one array doesn't have 0s and < the other array after replacing all 0's with 1's, reteurn -1
    #3. replace 0's with 1's and return the bigger sums

        count1 = nums1.count(0)
        count2 = nums2.count(0)

        sums1 = sum(nums1)
        sums2 = sum(nums2)
        
        min1 = sums1 + count1
        min2 = sums2 + count2

        if count1 == 0 and min2 > sums1:
            return -1
        if count2 == 0 and min1 > sums2:
            return -1

        return max(min1, min2)
