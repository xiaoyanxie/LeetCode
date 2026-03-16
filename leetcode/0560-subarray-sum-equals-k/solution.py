from collections import defaultdict 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        1,2,3 k=3

        prefixSumFreq = {
            0: 1
            3: 2
            5: 1
        }
        total = 6
      0 3 6  5  3 8  6
        3,3,-1,-2,5,-2
        3
        3,3,-1,-2
          3
          3,-1,-2,5,-2
               -2,5
                  5,-2

        total = 0
        prefixSum = 0
        for each num in nums:
            prefixSum += num
            if prefixSum - k in prefixFreq:
                total += prefixFreq[prefixSum - k]
            prefixFreq[prefixSum] += 1
        """

        total = 0
        prefixFreq = defaultdict(int)
        prefixFreq[0] = 1
        prefixSum = 0

        for num in nums:
            prefixSum += num
            if (prefixSum - k) in prefixFreq:
                total += prefixFreq[prefixSum - k]
            prefixFreq[prefixSum] += 1
        
        return total
