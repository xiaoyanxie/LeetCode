class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2,1,-3,4,-1,2,1,-5,4]
        #                      ^
        # maxSum: 6
        # sum: 5

        currSum = -inf
        maxSum = -inf
        for n in nums:
            currSum = max(currSum + n, n)
            maxSum = max(currSum, maxSum)
        return maxSum
