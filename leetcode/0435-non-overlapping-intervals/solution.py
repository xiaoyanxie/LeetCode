class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prevEnd = -inf

        removed = 0
        for start, end in intervals:
            # when we find an non-overlapped interval, append it
            if start < prevEnd:
                removed += 1
            else:
                prevEnd = end
        
        return removed
