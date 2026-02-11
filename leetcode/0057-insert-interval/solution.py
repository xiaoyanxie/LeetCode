class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(result):
            merged = [result[0]]
            for i in range(1, len(result)):
                interval = result[i]
                if merged[-1][1] >= interval[0]:
                    #merge
                    merged[-1][1] = max(merged[-1][1], interval[1])
                else:
                    merged.append(interval)
            return merged
    
        # l = 0
        # r = len(intervals)
        # while l < r:
        #     mid = l + (r - l) // 2
        #     if intervals[mid][0] == newInterval[0]:
        #         result = intervals[:mid] + [newInterval] + intervals[mid:]
        #         return merge(result)

        #     if intervals[mid][0] < newInterval[0]:
        #         l = mid + 1
        #     else:
        #         r = mid
        
        # if 0 <= l < len(intervals) and intervals[l][0] >= newInterval[0]:
        #     result = intervals[:l] + [newInterval] + intervals[l:]
        #     return merge(result)
        # else:
        #     result = intervals[:l + 1] + [newInterval] + intervals[l + 1:]
        #     return merge(result)

        index = bisect.bisect_left(intervals, newInterval)
        intervals.insert(index, newInterval)
        return merge(intervals)
