class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)

        # count = sorted(count.keys(), key = lambda x: count[x], reverse = True)

        # return count[0:k]
        heap = []
        for key in count.keys():
            if len(heap) < k:
                heapq.heappush(heap, (count[key], key))
            else:
                if heap[0][0] < count[key]:
                    heapq.heappushpop(heap, (count[key], key))
        res = []         
        for h in heap:
            res.append(h[1])
        return res
