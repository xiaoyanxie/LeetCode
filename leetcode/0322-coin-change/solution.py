from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([ (amount, 0) ])
        visited = set()
        while queue:
            remaining, changes = queue.popleft()

            if remaining == 0:
                return changes

            for coin in coins:
                nxt_remaining = remaining - coin
                if nxt_remaining >= 0 and nxt_remaining not in visited:
                    visited.add(nxt_remaining)
                    queue.append( (nxt_remaining, changes + 1) )

        return -1
