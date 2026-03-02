from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        (a, b, 2), (b, c, 3)

        a -2-> b -3-> c

        (a, b, 1.5), (b, c, 2.5), (bc, cd, 5.0)
        a -1.5-> b -2.5-> c
        bc -5.0-> cd
        """

        # 'a' -> { (b, 2) }
        # 'b' -> { (c, 3) }
        graph = {}
        
        for i, quation in enumerate(equations):
            var1, var2 = quation
            value = values[i]
            if var1 not in graph:
                graph[var1] = {}
            graph[var1][var2] = value
            if var2 not in graph:
                graph[var2] = {}
            graph[var2][var1] = 1 / value

        result = []

        """
         a -1.5-> b -2.5-> c
        bc -5.0-> cd
        {
            a: {b:1.5},
            b: {a:1/1.5},{c:2.5},
            c: {b:1/2.5},
            bc: {cd:5.0},
            cd: {bc:1/5.0}
        }
        """

        def dfs(v, target, visited):
            if v not in graph:
                return -1.0
            if target in graph[v]:
                return graph[v][target]
            visited.add(v)
            for adj in graph[v]:
                if adj in visited:
                    continue
                value = dfs(adj, target, visited)
                if value != -1.0:
                    return graph[v][adj] * value
            return -1.0

        for q1, q2 in queries:
            value = dfs(q1, q2, set())
            # print(f'{q1}->{q2}={value}')
            result.append(value)

        return result
