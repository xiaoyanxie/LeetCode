class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        # if r < 0:
        #     return []
        for i, n in enumerate(numbers):
        #     if l == r == 0:
        #         return [1]
            while l < r:
                added = numbers[l] + numbers[r]
                if added == target:
                    return [l+1, r+1]
                elif added < target:
                    l += 1
                else:
                    r -= 1
        # return []



