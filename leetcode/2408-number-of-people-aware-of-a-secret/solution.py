from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        activeSharing = 0
        queue = deque([1])
        for i in range(1, n):
            if len(queue) == forget:
                # handle forget
                activeSharing -= queue.popleft()
            
            wokeUp = len(queue) - delay
            if wokeUp >= 0:
                activeSharing += queue[wokeUp]
            queue.append(activeSharing)
        
        return sum(queue) % (10**9 + 7)
            
