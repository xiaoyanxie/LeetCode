class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # used = set()
        # for i in intervals:
        #     start = i[0]
        #     end = i[1]
        #     for j in range(start, end):
        #         if j in used:
        #             return False
        #         else:
        #             used.add(j)
        
        # return True

# Get each interval by itrating the list of list, then put the number in this interval into the set if the set doesn't contain, return false if the set contains the number.
#Time complexity: #interval * # element in one interval: O(N * K).
#Space complexity: O(N*K)
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                continue
            elif intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True
