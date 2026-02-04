class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # from collections import Counter
        # hmap = Counter(nums)
        # res = 0
        # for key in hmap.keys():
        #     #if not exist a pair, continue
        #     if k - key in hmap:
        #     #if exist a pair, use up
        #         while hmap[key]:
        #             hmap[key] -=1
        #             if hmap[k-key] == 0:
        #                 hmap[key] +=1
        #                 break
        #             else:
        #                 hmap[k-key] -=1
        #                 res +=1
        # return res
        hmap = {}
        res = 0
        for num in nums:
            if k - num in hmap and hmap[k-num] != 0:
                hmap[k-num]-=1
                res +=1
            else:
                if num in hmap:
                    hmap[num] += 1
                else:
                    hmap[num] = 1

        return res
