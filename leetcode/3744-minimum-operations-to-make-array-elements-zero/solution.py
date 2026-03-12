class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        """
        nums = [n, n + 1, n + 2, ..., n + m]

        nums[i] // 2

        log4(nums[i])


        """
        def steps(n):
            return math.floor(math.log(n, 4)) + 1

        def numOps(l, r) -> int:
            heap = [ (-steps(n), n) for n in range(l, r + 1) ]
            heapq.heapify(heap)
            # print(f'heap={heap}')
            ops = 0
            while len(heap) >= 2:
                _, n1 = heapq.heappop(heap)
                _, n2 = heapq.heappop(heap)
                # print(f'choose ({n1}, {n2}) in {[n for stps, n in heap]}')
                n1 //= 4
                n2 //= 4
                if n1 > 0:
                    heapq.heappush(heap, (-steps(n1), n1))
                if n2 > 0:
                    heapq.heappush(heap, (-steps(n2), n2))
                ops += 1
            
            if heap:
                stps, _ = heap.pop()
                ops += abs(stps)
            print(f'{r - l + 1} elements takes {ops} ops')
            return ops

        def prefixSteps(n):
            # return sum(steps(n) for n in range(1, n + 1))
            steps = 0
            p = 1
            k = 1

            while p <= n:
                steps += k * ((min(p * 4 - 1, n) - p) + 1)
                p *= 4
                k += 1

            return steps
            
        total = 0
        for l, r in queries:
            # print(prefixSteps(r), prefixSteps(l - 1))
            total += math.ceil((prefixSteps(r) - prefixSteps(l - 1)) / 2)
        return total
