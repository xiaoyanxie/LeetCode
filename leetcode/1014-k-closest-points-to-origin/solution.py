class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for point in points:
            dis = ((point[0]**2 + point[1]**2)) **0.5
            tup = [-dis, point]
            if len(heap) < k:
                heapq.heappush(heap, tup)
            elif len(heap) == k:
                if heap[0][0] >= -dis:
                    continue
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, tup)
        
        res = []
        for ele in heap:
            res.append(ele[1])
        
        return res

        # first get the distance from point to origin for every point, and then point, distance as a tuple for heap nodes.O(n)
        #for the smallest k distances, minheapO(logk)->return related points O(k)
        #=>O(nlogk) overall runtime


        
        
