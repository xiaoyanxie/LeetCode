class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # [2,3,6,7]
        # 2 (5) -> 2,3
        #       -> 2 (3) -> 2, 3
        #       -> 3 (1) -> None

        combinations = []
        candidates.sort()

        def dfs(remaining, i, combination):
            if remaining == 0:
                combinations.append(list(combination))
                return
            if remaining < 0:
                return

            # for c in candidates:
            for i in range(i, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break
                combination.append(c)
                dfs(remaining - c, i, combination)
                combination.pop()

        dfs(target, 0, [])

        return combinations
