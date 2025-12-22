class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range (0, len(nums)):
            if k >0 and nums[k] == nums[k-1]:
                continue

            i = k + 1
            j = len(nums) - 1
            comp = -nums[k]
            while i < j:
                s = nums[i] + nums[j]
                if s == comp:
                    res.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i] == nums[i+1]:
                        i+=1
                    while i < j and nums[j] == nums[j-1]:
                        j-=1
                    i+=1
                    j-=1
                elif s > comp:
                    j-=1
                elif s < comp:
                    i+=1
        return res
