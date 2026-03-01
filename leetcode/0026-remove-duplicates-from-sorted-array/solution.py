from collections import deque
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        []
        curr = 0
        [0,1,2,3,4,2,2,3,3,4]
         ^
        """
        queue = deque()
        curr = nums[0]
        cnt = 1
        for i, num in enumerate(nums):
            if i == 0: continue
            if num == curr:
                queue.append(i)
                continue
            
            curr = num
            cnt += 1

            if queue:
                nums[queue.popleft()] = num
                queue.append(i)

        for i in queue:
            nums[i] = '_'

        return cnt
