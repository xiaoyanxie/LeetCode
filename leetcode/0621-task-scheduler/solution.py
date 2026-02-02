class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        import heapq

        freq = Counter(tasks)
        
        heap = []
        for task in freq:
            heapq.heappush(heap, (-freq[task], task))

        res = 0

        while heap:
            used = 0
            tmp= []
            for i in range(n+1):
                if not heap:
                    break
                
                count,task = heapq.heappop(heap)
                count = -count
                count -=1
                used+=1
                if count > 0:
                    tmp.append((-count, task))
                    

            # res += subres
            for item in tmp:
                heapq.heappush(heap,item)
                tmp = []
            if heap:
                res += n + 1
            else:
                res += used
        return res
        
        
