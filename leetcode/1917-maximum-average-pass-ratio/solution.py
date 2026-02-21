import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # [1,2],[3,5],[2,2]

        def gain(passi, totali):
            return ((1 + passi) / (1 + totali)) - (passi / totali)

        maxheap = []
        for i in range(len(classes)):
            passi = classes[i][0]
            totali = classes[i][1]
            heapq.heappush(maxheap, (-gain(passi, totali), passi, totali))
        
        # print(maxheap)
        while extraStudents > 0:
            _, passi, totali = heapq.heappop(maxheap)
            
            # add the student
            newPassi, newTotali = passi + 1, totali + 1
            extraStudents -= 1

            heapq.heappush(maxheap, (-gain(newPassi, newTotali), newPassi, newTotali))

        # print(maxheap)
        total = 0
        for _, passi, totali in maxheap:
            total += passi / totali
        return total / len(classes)
