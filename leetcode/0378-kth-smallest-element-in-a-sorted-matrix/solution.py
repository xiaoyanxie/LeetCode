class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        # heap = []
        # count = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if count < k:
        #             heapq.heappush(heap, -matrix[i][j])
        #             count += 1
        #         elif count == k:
        #             if matrix[i][j] < -heap[0]:
        #                 heapq.heappushpop(heap, -matrix[i][j])
        # return -heap[0]

        heap = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(min(row, k)):
            heap.append((matrix[i][0], i, 0))
        heapq.heapify(heap)
        cnt = 0
        while cnt < k:
            num, i, j = heapq.heappop(heap)
            cnt += 1
            if cnt == k:
                return num
            if j + 1 < col:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        
            



        
        
