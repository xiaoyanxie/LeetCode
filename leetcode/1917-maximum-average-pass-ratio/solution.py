import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
               sum(pi / ti)
        P = -----------------
               len(classes)
        
        gain = (pi + 1) / (ti + 1) - pi / ti
        """

        def gain(i, assigned):
            pi = classes[i][0] + assigned
            ti = classes[i][1] + assigned
            return (pi + 1) / (ti + 1) - pi / ti

        # 1. init the heap with gain calculated by assigning 1 student to each class
        # (gaini, assigned, i)
        heap = []
        for i in range(len(classes)):
            heap.append((-gain(i, 0), 0, i))

        heapq.heapify(heap)

        # 2. for each student:
        #        pop the class with the max gain
        #        assign one student to the class
        for _ in range(extraStudents):
            # print(f'gains: {[ -gain for gain, _, _ in heap ]}')
            gaini, n, i = heapq.heappop(heap)
            n += 1
            # print(f'add 1 student to class [{i}] because gain={-gaini} -> {classes[i][0] + n}/{classes[i][1] + n}')
            heapq.heappush(heap, (-gain(i, n), n, i))

        # 3. for all classes, calculate the avg pass ratio
        return sum( (classes[i][0] + n) / (classes[i][1] + n) for _, n, i in heap ) / len(classes)
