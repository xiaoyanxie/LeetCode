class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #put kth largesst numbers in min heap
        self.heap = []
        self.size = len(self.heap)
        self.k = k
        for num in nums:
            if self.size == k:
                if num > self.heap[0]:
                    heapq.heappushpop(self.heap, num)
            else:
                heapq.heappush(self.heap, num)
                self.size += 1
    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.heap, val)
            self.size += 1
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        
        return self.heap[0]

    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#min heap to maintain the top k largest element, each time, when calling add, return the root of the heap
