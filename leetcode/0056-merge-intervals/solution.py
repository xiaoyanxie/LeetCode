class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge(l: List[int], r: List[int]) -> bool:
            if l[1] < r[0]:
                return False
            l[1] = max(l[1], r[1])
            return True
        
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            elif not merge(merged[-1], interval):
                merged.append(interval)
        
        return merged
