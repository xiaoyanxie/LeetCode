class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        container = set()
        count = 0
        length = 0
        for num in nums:
            container.add(num)
        
        # for num in nums:
        #     if(num + 1 not in container) and (num - 1 not in container):
        #         container.discard(num)
        # for num in nums:
        #     if (num + 1 in container) and (num - 1 not in container):
        #         while num in container:
        #             count = count + 1
        #             num = num + 1
        #         length = max(length, count)  
        #         count = 0 

        for num in container:
            # find the min value to start
            if num - 1 not in container: # and num + 1 in container:
                #                          ^
                #                          这个条件不能加，加了会导致 [0] 或者 [0,0] 这种 case 过不了，少算了长度为1的情况
                while num in container:
                    count = count + 1
                    num = num + 1
                length = max(length, count)
                count = 0

        return length 

