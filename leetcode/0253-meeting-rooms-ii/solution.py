class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [0, 30] [5, 10][15,20]
        heap = [30]
        heap = [10,30]
        heap = [30]
        [2,4][7,10]
        heap = [4]
        """
        if len(intervals) == 1:
            return 1
        intervals.sort()

        heap = [intervals[0][1]]
        for interval in intervals[1:]:
            if interval[0] < heap[0]:
                heapq.heappush(heap, interval[1])
            else:
                heapq.heappop(heap)
                heapq.heappush(heap ,interval[1])
        
        return len(heap)

