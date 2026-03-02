from collections import deque

class HitCounter:

    def __init__(self):
        self.queue = deque() # (1, 1), (2, 1), (3, 1), (300, 1)

    """
    [[], [1], [2], [3], [4], [300], [300], [301]]
    """

    def hit(self, timestamp: int) -> None:
        """
        [ (ts1, cnt1), (ts1, cnt1), ... ]
        """
        # shrink the. window
        while self.queue and timestamp - self.queue[0][0] > 300:
            self.queue.popleft()
        
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        """
        1, 2, 101, 105, 200, ..., 301
        l
                          r


        getHits(300) = 2
        getHits(301)

        returns (timestamp - 300, timestamp]
        """
        # i = bisect.bisect_right(self.queue, timestamp - 300, key=lambda x: x[0])
        
        l, r = 0, len(self.queue) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.queue[mid][0] <= timestamp - 300:
                l = mid + 1
            else:
                r = mid - 1

        # assert l == bisect.bisect_right(self.queue, timestamp - 300, key=lambda x: x[0])

        i = l
        # assert 0 <= l < len(self.queue)

        total = 0
        while i < len(self.queue) and self.queue[i][0] <= timestamp:
            total += self.queue[i][1]
            i += 1
        return total

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
