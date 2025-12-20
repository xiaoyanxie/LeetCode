class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                continue
            elif intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True

# Get sorted list of intervals, which means the intervals are sorted by the first ele then by the second ele. Then compare the start time of current interval with the ending time of the last interval to find out if there is overlap

#Time complexity: sort: O(nlogn), compare O(n) where n is the number of intervals. overall runtime: O(nlogn)

#space complexity: sort is in place O(n), for python sort algo is a combination of Merge sort and insertion sort, compare takes extra O(1) space. ovrall space complexity is O(n)


