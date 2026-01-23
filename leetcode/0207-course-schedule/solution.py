class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:           
        if not prerequisites:
            return True

        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        def dfs(prereq):
            if state[prereq] == 2:
                return True
            if state[prereq] == 1:
                return False

            state[prereq] = 1
            for c in adj[prereq]:
                if not dfs(c):
                    return False
            state[prereq] = 2
            return True

        state = [0] * numCourses
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        
        return True
