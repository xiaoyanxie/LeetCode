class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtracking(path, target, start):
            if target == 0:
                res.append(list(path))
            

            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    backtracking(path, target - candidates[i], i)
                    path.pop()
                else:
                    break
        backtracking([], target, 0)

        return res
