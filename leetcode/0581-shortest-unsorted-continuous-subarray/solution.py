class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        maxseen = -inf
        minseen = inf
        l, r = -1, -1
        for i in range(len(nums)):
            n = nums[i]
            if n < maxseen:
                r = i
            maxseen = max(n, maxseen)
        
        for i in reversed(range(len(nums))):
            n = nums[i]
            if n > minseen:
                l = i
            minseen = min(n, minseen)
        
        """
        In the array, if there is at least one pair i and j out of order, then:
        i < j and nums[i] > nums[j]

        In the above we got furthest l that satisfies nums[l] > nums[j], so l <= i
        In the above we got furthest r that satisfies nums[r] < nums[i], so j <= r
        Therefore: l <= i < j <= r
        So when there is at least one pair of numbers out of order, then l < r
        """

        if l < r:
            return r - l + 1
        return 0
