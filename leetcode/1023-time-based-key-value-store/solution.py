from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]

        if not values:
            return ''
        
        i, j = 0, len(values)
        while i < j:
            mid = i + (j - i) // 2
            if values[mid][1] <= timestamp:
                i = mid + 1
            else:
                j = mid
        
        if j == 0:
            return ''
        
        return values[j - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
