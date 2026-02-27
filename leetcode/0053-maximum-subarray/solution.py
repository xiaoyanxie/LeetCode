from collections import defaultdict
import heapq
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """

        i -> j: sum(nums[i:j + 1])
        """

        best = -inf
        minRunningSum = 0
        runningSum = 0
        for i, n in enumerate(nums):
            runningSum += n
            if runningSum - minRunningSum > best:
                best = runningSum - minRunningSum
            # heapq.heappush(runningSums, runningSum)
            if minRunningSum > runningSum:
                minRunningSum = runningSum
        return best
