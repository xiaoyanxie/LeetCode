import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = []
        for n in nums:
            if n in top3:
                continue
            if len(top3) < 3:
                heapq.heappush(top3, n)
            elif n > top3[0]:
                heapq.heappop(top3)
                heapq.heappush(top3, n)
        
        if len(top3) == 1 or len(top3) >= 3:
            return top3[0]
        
        heapq.heappop(top3)
        return top3[0]
