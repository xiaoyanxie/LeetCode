class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        from sortedcontainers  import SortedList 
        sl = SortedList(nums[:k])   
        res = []
        def findMedian():
            if k % 2 == 1:
                return sl[k//2]
            else:
                return (sl[k//2 -1] + sl[k // 2]) /2.0
        res.append(findMedian())

        for i in range(len(nums) - k):
            if i < len(nums) - k:
                sl.remove(nums[i])
            
                sl.add(nums[i+k])
            res.append(findMedian())
        return res        
        #     lmaxh = []
        #     rminh = []
        #     for num in nums:
        #         if k % 2 == 0:
        #             if len(lmaxh) == k//2:
        #                 if num < -lmaxh[0]:
        #                     tmp = -heapq.heappop(lmaxh)
        #                     heapq.heappush(rminh,tmp)
        #                     heapq.heappush(lmaxh,-num)
        #                 else:
        #                     heapq.heappush(rminh,num)
        #             else:
        #                 heapq.heappush(lmaxh,-num)
        #         else:
        #             if len(lmaxh) == k//2 + 1:
        #                 if num < -lmaxh[0]:
        #                     tmp = -heapq.heappop(lmaxh)
        #                     heapq.heappush(rminh,tmp)
        #                     heapq.heappush(lmaxh,-num)
        #                 else:
        #                     heapq.heappush(rminh,num)
        #             else:
        #                 heapq.heappush(lmaxh,-num)
                    
        #     if k % 2 == 0:
        #         return (-lmaxh[0] + rminh[0])/2
        #     else:
        #         return -lmaxh[0]

        # i = 0
        # j = i + k - 1
        # res = []
        # while j < len(nums):
        #     med = findMidean(nums[i:j + 1])
        #     res.append(med)
        #     i += 1
        #     j += 1
        
        # return res
        
