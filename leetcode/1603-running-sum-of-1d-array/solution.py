class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        ret = []
        for n in nums:
            acc += n
            ret.append(acc)
        return ret
