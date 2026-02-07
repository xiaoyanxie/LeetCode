import heapq
from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = defaultdict(int)
        # for num in nums:
        #     freq[num] += 1
        
        # heap = []
        # for num, f in freq.items():
        #     heapq.heappush(heap, (-f, num))

        # return [ heapq.heappop(heap)[1] for _ in range(k) ]
        return [item for item, count in Counter(nums).most_common(k)]
