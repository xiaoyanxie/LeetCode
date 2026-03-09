from collections import deque
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        n = 6, delay = 2, forget = 4

        day: 0 1 2 3 4 5 6 7 8 9
             1 0 1 1 1 2
                   |del|
               | forget|
        """
        window = deque([1])
        sharing = 0 # 2
        for day in range(1, n): # 4
            # sum of (day - forget, day - delay]
            if len(window) >= delay:
                sharing += window[len(window) - delay]

            # shrink
            if len(window) >= forget:
                sharing -= window.popleft()
            
            # share
            window.append(sharing)
            # print(f'day={day + 1}, window={window}, sharing={sharing}')
        
        return sum(window) % (10 ** 9 + 7)
