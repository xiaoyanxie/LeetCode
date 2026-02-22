class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l = i + 1
            r = n - 1

            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l<r and nums[l+1] == nums[l]:
                        l += 1
                    while l<r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return res
