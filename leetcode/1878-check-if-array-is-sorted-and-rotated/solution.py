class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True
            
        count = 0
        for i in range(l):
            if nums[i] > nums[(i + 1)%l]:
                if count == 1:
                    return False
                count = 1
        return True

# Sorted and rotated array can be visualized as a circular sequence, and there will be no more than 1 drop. Find the drop by comparing an element with the next one

# The complexity is O(n) because we iterate over the array once
# It takes O(1) extra space since we only need extra space to compare the elements with the next one
