class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif len(heap) >= k:
                if num < heap[0]:
                    continue
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        
        return heap[0]


