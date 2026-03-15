class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1,2,3,|4,5,6,7
                     j

        4,5,6|7,1,2,3
            i   j

        1,2,3,4,5,6,|7
        7,5,4,3,2,1,|6
          i            
                  j

        6,7,1,2,3,|4,5
              i
              j

        4,5,6,|7,1,2,3
               i                     
               j

        3,4,|7,6,5,1,2
             i
                 j

        1. reverse the two parts
        2. fix i, j to 0, len(nums) - 1, swap inwards
        """
        def rev(a, l, r):
            while l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1

        k %= len(nums)
        rev(nums, 0, len(nums) - k - 1)
        rev(nums, len(nums) - k, len(nums) - 1)
        rev(nums, 0, len(nums) - 1)

