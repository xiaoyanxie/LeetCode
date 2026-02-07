class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # [2,3,6,7]

        # res = set()
        res = []
        candidates.sort()

        def dfs(remaining, i, combination):
            if remaining == 0:
                # res.add(tuple(sorted(combination)))
                res.append(list(combination))
            
            for j in range(i, len(candidates)):
                c = candidates[j]
                if c > remaining:
                    break
                combination.append(c)
                dfs(remaining - c, j, combination)
                combination.pop()

        dfs(target, 0, [])

        # return list(res)
        return res
