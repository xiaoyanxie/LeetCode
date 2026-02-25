class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twoSum(exclude, n):
            ret = []
            i, j = exclude + 1, len(nums) - 1
            while i < j:
                a, b = nums[i], nums[j]
                if a + b + n == 0:
                    ret.append([a, b, n])
                    while i < j and nums[i] == a:
                        i += 1
                    while i < j and nums[j] == b:
                        j -= 1
                elif a + b + n < 0:
                    while i < j and nums[i] == a:
                        i += 1
                else:
                    while i < j and nums[j] == b:
                        j -= 1
            return ret
        
        ret = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            ret += twoSum(i, n)
        return ret
