class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        
        @cache
        def dfs(i, nCityA, nCityB) -> int:
            """
            Time: O(N^2)
            Space: O(N^2)
            """
            if nCityA + nCityB == 2 * N:
                assert i == len(costs)
                return 0
            
            if nCityA == N:
                return costs[i][1] + dfs(i + 1, nCityA, nCityB + 1)
            elif nCityB == N:
                return costs[i][0] + dfs(i + 1, nCityA + 1, nCityB)
            else:
                cost1 = costs[i][1] + dfs(i + 1, nCityA, nCityB + 1)
                cost2 = costs[i][0] + dfs(i + 1, nCityA + 1, nCityB)
                return min(cost1, cost2)


        def greedy():
            """
            Time: O(N * log(N))
            Space: O(N)
            """
            total = sum(a for a, _ in costs)

            diff = [0] * (N * 2)
            for i, cost in enumerate(costs):
                diff[i] = (cost[1] - cost[0], i)
            
            diff.sort(key=lambda x: x[0])

            for i in range(N):
                extra, j = diff[i]
                total += extra
            
            return total
        
         # return dfs(0, 0, 0)
        return greedy()
