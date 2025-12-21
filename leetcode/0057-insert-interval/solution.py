class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start,end])
            else:
                res[-1][1] = max(end, res[-1][1])
        return res


