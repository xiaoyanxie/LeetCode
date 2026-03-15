class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = [intervals[0]]
        """
        ret: [[1,  10], [15,      18]]

        [1,  3],  
          [2,        6],
                [4,      9]
                      [8,    10],     [15,      18]
        """
        for i, [start, end] in enumerate(intervals):
            if i == 0: continue
            if start <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], end)
            else:
                ret.append([start, end])
        return ret
