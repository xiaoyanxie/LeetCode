class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        [1,  3],
          [2,    6],
                     [8,        10], [15,       18]

        [1,  3],
            [3,   6],
                     [8,        10], [15,       18]
        
        [1,  3],
            [3,   6],       [9, 10]
                     [8,           11], 
        """

        intervals.sort()
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            if ret[-1][1] >= intervals[i][0]:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
            else:
                ret.append(intervals[i])
        return ret
