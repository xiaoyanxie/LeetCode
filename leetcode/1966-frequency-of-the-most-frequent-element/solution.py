import heapq
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
         0+1+0+3
        steps += (nums[r] - nums[r - 1]) * (r - l)
        [3,4,4,5,5,5,5,6,13] k=3 left=0
           l
               r
        5: 4
        4: 2
        3: 1
        6: 1
        13:1

        3 (1) -1-> 4 (2) -1-> 5 (4) -1-> 6 (1) -7-> 13 (1)
        """
        nums.sort()
        maxfreq = 0
        l = 0
        # @cache
        # def steps(i, j):
        #     delta = 0
        #     for k in range(i + 1, j + 1):
        #         a, b = nums[k - 1], nums[k]
        #         delta += (b - a) * (k - i)
        #     # print(f'steps({i},{j})={delta}')
        #     return delta
        curr = 0

        for r in range(len(nums)):
            # shrink the window
            # while steps(l, r) > k:
            #     l += 1

            curr += nums[r]

            while nums[r] * (r - l + 1) - curr > k:
                curr -= nums[l]
                l += 1
            
            maxfreq = max(maxfreq, r - l + 1)
        return maxfreq
