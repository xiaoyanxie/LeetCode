class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        earliestEndTimes = []
        
        for start, end in intervals:
            if earliestEndTimes and earliestEndTimes[0] <= start:
                heapq.heappop(earliestEndTimes)
            heapq.heappush(earliestEndTimes, end)
        
        return len(earliestEndTimes)
