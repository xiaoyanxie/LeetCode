class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      
        if len(intervals) == 0:
            return [newInterval]

        res = []
        
       # check current, if first less than new interval's first, add to res
        # if first equal or bigger than interval's first:
        #add modified interval, 
        #for the rest, check the end of interval , if less than res-1's end, continue, if first bigger than res's second, append, if first less than res 's second and second bigger than interval's second, update
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        res.append(newInterval)
      
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
        
        
