class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        room: 2
        [[0,30],[5,10],[15,20]]
        [0,30],[5,10]

        [0,                                      30]
                [5,   10]
                     [10,11]
                             [15,       20]
                                     [18,     23]
        
        heap: 20,23,30
        """
        intervals.sort()
        heap = []
        for i, interval in enumerate(intervals):
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return len(heap)
