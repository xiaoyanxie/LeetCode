import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        (pass1 / total1) + (pass2 / total2) + (pass3 / total3) + ...
        ------------------------------------------------------------ = avg_pass_ratio
                                    N
        
        max(
            (pass1 / total1) + (pass2 / total2) + (pass3 / total3) + ...
        )

        Use a minheap to sort by total_i, then pass_i
        
        [1,2],[3,5],[2,2]
        (1,2) (0.66666,0) (0.6,1)
        """
        def gain(passi, totali):
            return ((passi + 1) / (totali + 1)) - (passi / totali)

        # build heap
        heap = []
        for passi, totali in classes:
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))

        while extraStudents > 0:
            # assign the student to the smallest pass rate class first each time
            _, passi, totali = heapq.heappop(heap)
            
            passj, totalj = passi + 1, totali + 1
            heapq.heappush(heap, (-gain(passj, totalj), passj, totalj))
            extraStudents -= 1
        
        # calculate the avg num
        sumall = 0
        for _, passi, totali in heap:
            sumall += (passi / totali)
        return sumall / len(classes)
