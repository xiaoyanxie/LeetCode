import heapq

class Bucket:
    def __init__(self,size,ops):
        self.size = size
        self.ops = ops

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        """
        40,[41,42],[43,44],[45,46],[47,48]

        48 -> 12 -> 3 -> 0
        46 -> 11 -> 2 -> 0
        44 -> 11 -> 2 -> 0
        42 -> 10 -> 2 -> 0
        """
        def simulate(start, end):
            maxheap = []
            cnt = 0
            for n in range(start, end + 1):
                heapq.heappush(maxheap, -n)
            
            while len(maxheap) >= 2:
                a = -heapq.heappop(maxheap)
                b = -heapq.heappop(maxheap)
                a, b = math.floor(a / 4), math.floor(b / 4)
                cnt += 1
                if a > 0:
                    heapq.heappush(maxheap, -a)
                if b > 0:
                    heapq.heappush(maxheap, -b)
            if maxheap:
                cnt += (math.floor(math.log(-maxheap[0], 4)) + 1)
            return cnt

        def splitBuckets(start, end):
            opsLo = math.floor(math.log(start, 4)) + 1
            opsHi = math.floor(math.log(end, 4)) + 1
            buckets = []
            for k in range(opsLo, opsHi + 1):
                startk = start if k == opsLo else 4**(k - 1)
                endk = end if k == opsHi else 4**k - 1
                buckets.append([endk - startk + 1, k])
            return buckets

        def count(start, end):
            """
            [4^0      ,4^1 - 1] -> 1
            [4^1      ,4^2 - 1] -> 2
            [4^2      ,4^3 - 1] -> 3
            [4^3      ,4^4 - 1] -> 4
            [4^(k - 1),4^k - 1] -> k
            
            Example:
            [4,63] = [4,15] + [16,63]
            [a,b] = [bucket1] + [bucket2] + [bucket3] + ... + [bucketN]

            Pseudo-code for each bucket:
            queryi = [a, b]
            buckets = splitBuckets(queryi) # ordered asc

            ops = 0
            largest = buckets.pop()
            while buckets:
                nxt = buckets.pop()
                ops += math.ceil(largest.size * (largest.ops - nxt.ops) / 2)
                nxt.size += largest.size
                largest = nxt
            
            ops += math.ceil(largest.size * largest.ops / 2)
            """
            buckets = splitBuckets(start, end)
            # print(buckets)
            ops = 0
            largest = buckets.pop()
            while buckets:
                nxt = buckets.pop()
                ops += largest[0] * (largest[1] - nxt[1]) / 2
                nxt[0] += largest[0]
                largest = nxt

            ops += largest[0] * largest[1] / 2
            return math.ceil(ops)

        cnt = 0
        for start, end in queries:
            # cnt += simulate(start, end)
            cnt += count(start, end)
        return cnt
