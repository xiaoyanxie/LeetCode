class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        imax = nums[0]
        imin = nums[0]

        for n in nums[1:]:
            tmp = imax
            imax = max(n, n * tmp, n * imin)
            imin = min(n, n * tmp, n * imin)
            res = max(imax, res)

        return res
       
