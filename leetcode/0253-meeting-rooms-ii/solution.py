class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        rooms: 3
        [0,                                              30],
             [5,       10],  
                         [11,12],
                             [12,     16]
                                   [15,      20]
        """
        intervals.sort(key=lambda x: x[0])
        heap = [] # [16,20,30]
        for interval in intervals:
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return len(heap)
