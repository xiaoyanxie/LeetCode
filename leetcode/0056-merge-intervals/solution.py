class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            a,b = res[-1]
            if intervals[i][0] <= b and intervals[i][1] > b:
                res[-1][1] = intervals[i][1]
            elif intervals[i][0] > b:  
                res.append(intervals[i])
        
        return res

