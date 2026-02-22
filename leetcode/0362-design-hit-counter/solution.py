from collections import deque
class HitCounter:

    def __init__(self):
        self.window = deque()

    def hit(self, timestamp: int) -> None:
        # [ [ts, cnt], ... ]
        while self.window and timestamp - self.window[0][0] > 300:
            self.window.popleft()
        
        if self.window and timestamp == self.window[-1][0]:
            self.window[-1][1] += 1
        else:
            self.window.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        i = bisect.bisect_right(self.window, timestamp - 300, key=lambda x: x[0])
        # [timestamp - 300, timestamp]
        #         i
        total = 0
        while i < len(self.window) and self.window[i][0] <= timestamp:
            total += self.window[i][1]
            i += 1
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
