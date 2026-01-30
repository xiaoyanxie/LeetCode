class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, path,remain):
            if remain == 0:
                res.append(path.copy())
                return
            
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, remain-candidates[i])
                if path:
                    path.pop()

        dfs(0, [], target)
        return res
