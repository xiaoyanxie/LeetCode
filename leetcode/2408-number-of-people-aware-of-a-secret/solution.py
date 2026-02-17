from collections import deque
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        """
        1     0     1     1     1     2
        day1  day2  day3  day4  day5  day6
        ^
    ^   ^
        """

        # sliding window
        queue = deque([1])
        activeSharing = 0
        for day in range(1, n):
            # shrink the queue
            if len(queue) == forget:
                activeSharing -= queue.popleft()
            
            lastActive = len(queue) - delay
            if lastActive >= 0:
                activeSharing += queue[lastActive]
            
            # print(f'day{day + 1}, {activeSharing} active sharing')
            queue.append(activeSharing)

        return sum(queue) % MOD

