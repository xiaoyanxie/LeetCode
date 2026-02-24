from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        
        """

        runningSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        cnt = 0
        for num in nums:
            runningSum += num
            # runningSum - prefixSum = k
            if (runningSum - k) in prefixSums:
                cnt += prefixSums[runningSum - k]
            prefixSums[runningSum] += 1
        return cnt
