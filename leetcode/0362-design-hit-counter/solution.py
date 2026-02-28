from collections import deque

class HitCounter:

    def __init__(self):
        # 300s window
        # [ (ts, count) ]
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        while self.queue and timestamp - self.queue[0][0] > 300:
            self.queue.popleft()
        
        if self.queue and timestamp == self.queue[-1][0]:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        """
        1,3,4
        """
        i = bisect.bisect_right(self.queue, timestamp - 300, key=lambda x: x[0])
        hits = 0
        
        while i < len(self.queue) and self.queue[i][0] <= timestamp:
            hits += self.queue[i][1]
            i += 1
        return hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
