class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [1,3],[2,6],[8,10],[15,18]
        """
        intervals.sort()
        ret = [intervals[0]]
        for i, interval in enumerate(intervals):
            if i == 0: continue
            start, end = interval
            if start <= ret[-1][1]:
                ret[-1][0] = min(start, ret[-1][0])
                ret[-1][1] = max(end, ret[-1][1])
            else:
                ret.append(interval)
        return ret
