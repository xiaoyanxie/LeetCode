class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMax = nums[0]
        prevMin = nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            vals = (num, num * prevMin, num * prevMax)
            prevMin = min(vals)
            prevMax = max(vals)
            maxProduct = max(maxProduct, prevMax)
        return maxProduct
