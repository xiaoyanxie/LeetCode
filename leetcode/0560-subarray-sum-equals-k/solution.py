from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        -8,-1,1  k=-8, total=-25 cnt=2  prefixes={0, -8, -17}
        -8 -9 -8
               i

        1,-1,0   k=0  total=0. cnt=2  prefixes={0, 1, 0}
             i
           
        Since the constraints says n can be negative,
        we might see multiple valid prefixes, 
        thus we need a counter to count the #prefixes we have encountered.
        
        In the below example:
        we need prefixes={ total-k : 2 } for both case1 and case2
        case1: |- total-k -|---- k ----|
        case2: |--- total-k --|-- k ---|
               [a1,a2,a3,a4,a5,a6,a7,a8,a9]
               |---------total---------|
        """
        seen=defaultdict(int)
        seen[0] = 1
        cnt = 0
        total = 0
        for i, n in enumerate(nums):
            total += nums[i]
            prefix = total - k
            if prefix in seen:
                cnt += seen[prefix]
            seen[total] += 1
        return cnt
