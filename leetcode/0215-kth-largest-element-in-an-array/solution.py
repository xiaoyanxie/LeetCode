class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        #maintain a minheap that stores exactly k numbers. Compare each number in nums with the root, if it is larger, pop the root and add the number in heap. return the root after iterating over the array
        #iterate over the nums array takes O(n), for each iteration, check, push, pop, worst case O(logk), overall O(nlogk)
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif len(heap) == k:
                if num <= heap[0]:
                    continue
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        
        return heap[0]

