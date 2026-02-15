class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # scan the array, create a total product
        total = 1
        zeroIdx = -1
        for i, num in enumerate(nums):
            # if more than one zero
            if num == 0:
                if zeroIdx != -1: return [0] * len(nums)
                else: zeroIdx = i
            else:
                total *= num
        
        if zeroIdx != -1:
            products = [0] * len(nums)
            products[zeroIdx] = total
            return products

        # if less than two zeros
        return [ int(total / num) for num in nums ]
