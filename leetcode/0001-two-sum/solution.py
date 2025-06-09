class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], i]
            else:
                hashMap[num] = i
        #nested for loop to check
        # length = len(nums)
        # for num in range(length):
        #     for i in range(num + 1, length):
        #         if(nums[num] + nums[i]) == target:
        #             return [num,i]
                
        # return False
