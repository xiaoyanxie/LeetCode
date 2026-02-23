class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        1 -> 1
        
        2 -> 2
        4 -> 1

        cost() = (nums[j] - nums[j - 1]) * (j - i + 1)
        while cost() > k:
            k += (nums[j - 1] - nums[i])
            i += 1
            

        1,1,2,2,4    k=5
          i
                j

        [1,2,4] k = 4, best = 0
         i
           j

        1,4,8,13  k = 5, best = 2
            i
              j

        3,9,6    k = 2, best = 1
          i
            j
        """
        nums.sort()
        i = 0
        best = 0
        def cost(i, j):
            return (nums[j] - nums[j - 1]) * (j - i)

        for j in range(len(nums)): # 1
            while cost(i, j) > k:
                k += (nums[j - 1] - nums[i])
                i += 1
            k -= cost(i, j)
            best = max(best, j - i + 1)
        return best
