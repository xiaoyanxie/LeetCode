class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [[5,10],[15,20],[0,30]]
                    i
                    j
        [[5,10],[7,8],[9,11]]

        [[2,11],[6,16],[11,16]]
                  i   
                         j
        """
        intervals.sort()
        heap = []
        for i in range(len(intervals)):
            starti, endi = intervals[i]
            if heap and starti >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, endi)

        return len(heap)
