from collections import deque
class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        1,2,3,4,5,6,7,8,9,10,11
          2   4   6   8   10
              4       8
                      8

        1,2,3,4,5,6,7,8,9,10,11,12
          2   4   6   8   10    12
          2       6       10
                  6        

        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22
          2   4   6   8   10    12.   14    16    18    20    22
              4       8         12          16          20
                      8                     16
                      8

        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23
          2   4   6   8   10    12.   14    16    18    20    22
              4       8         12          16          20
                      8                     16
                      8

        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24
          2   4   6   8   10    12.   14    16    18    20    22    24
          2       6       10          14          18          22
                  6                   14                      22
                                      14

        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
          2   4   6   8   10    12.   14    16    18    20    22    24
          2       6       10          14          18          22
                  6                   14                      22
                                      14

        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
          2   4   6   8   10    12.   14    16    18    20    22    24    26
              4       8         12          16          20          24
                      8                     16                      24
                                            16
        
        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27
          2   4   6   8   10    12.   14    16    18    20    22    24    26
              4       8         12          16          20          24
                      8                     16                      24
                                            16
        
40      1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
20        2,  4,  6,  8,  10,   12,   14,   16,   18,   20,   22,   24,   26,   28,   30,   32,   34,   36,   38,   40
10        2,      6,      10,         14,         18,         22,         26,         30,         34,         38
 5                6,                  14,                     22,                     30,                     38
 2                                    14,                                             30
 1                                                                                    30
        """
        # def bruteforce():
        #     nums = [n for n in range(1, n + 1)]
        #     print(f'steps={nums[1] - nums[0]} head={nums[0]}, remaining={len(nums)}')
        #     forward = True
        #     while len(nums) > 1:
        #         tmp = deque()
        #         i = 1
        #         if forward:
        #             for j in range(len(nums)):
        #                 if i % 2 == 0:
        #                     tmp.append(nums[j])
        #                 i += 1
        #             print(f'{'forward' if forward else 'backward'}, steps={tmp[1] - tmp[0] if len(tmp) > 1 else -1} head={tmp[0]}, remaining={len(tmp)}')
        #             forward = False
        #         else:
        #             for j in reversed(range(len(nums))):
        #                 if i % 2 == 0:
        #                     tmp.appendleft(nums[j])
        #                 i += 1
        #             print(f'{'forward' if forward else 'backward'}, steps={tmp[1] - tmp[0] if len(tmp) > 1 else -1} head={tmp[0]}, remaining={len(tmp)}')
        #             forward = True
                
        #         nums = tmp
        #     return nums[0]

        if n == 1:
            return 1

        forward = True
        remaining = n
        head = 1
        steps = 1
        while remaining > 1:
            if remaining % 2 == 0 and not forward:
                steps *= 2
                remaining //= 2
                # print(f'{'forward' if forward else 'backward'}, steps={steps}, head={head}, remaining={remaining}')
                forward = not forward
                continue
            
            head += steps
            steps *= 2
            remaining //= 2
            # print(f'{'forward' if forward else 'backward'}, steps={steps}, head={head}, remaining={remaining}')
            forward = not forward
            
        return head
