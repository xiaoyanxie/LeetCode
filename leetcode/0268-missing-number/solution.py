class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #put all numbers in set
        #check size of nums
        #check each number
        container = set()
        for number in nums:
            container.add(number)
        length = len(nums)

        for i in range(length + 1):
            if i not in container:
                return i

        return -1
