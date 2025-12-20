class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        used = []
        heapq.heappush(used,intervals[0][1])
        for i in range(1, len(intervals)):
            if (intervals[i][0]) >= used[0]:
                old = heapq.heappop(used)
                heapq.heappush(used,intervals[i][1])
            else:
                heapq.heappush(used,    intervals[i][1])
        return len(used)
        
