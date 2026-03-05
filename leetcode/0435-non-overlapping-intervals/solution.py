class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
  
        if len(intervals) == 1:
            return 0

        intervals.sort(key = lambda x: x[1])
        remove = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                remove += 1
            else:
                end = intervals[i][1]
        return remove
#[-100,-2],[1,2],[2,3],[3,4],[5,7]
#                    ^
#end = 3
