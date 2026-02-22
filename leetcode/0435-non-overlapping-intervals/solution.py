class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                cnt += 1
            else:
                prev[0] = min(intervals[i][0], prev[0])
                prev[1] = max(intervals[i][1], prev[1])
        return cnt
