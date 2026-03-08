class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums = [1234]
        #prefix product = [1,2,6,24]
        #idx: 1,12,123,1234^2^3^4
        #nums[-1] = [4321]
        #suffix product = [4,12,24,1]
                        #    ^3^2^1
                       #   idx: 4,43,432,4321
        prefix = []
        suffix = []
        product = 1
        n = len(nums)
        for num in nums:
            product *= num
            prefix.append(product)
        product = 1
        for i in range(n):
            product *= nums[n-1-i]
            suffix.append(product)

        res = [suffix[n -2]]
        for i in range(0, n - 2):
            res.append(prefix[i] * suffix[n - 3 - i])
        
        res.append(prefix[-2])
        return res
