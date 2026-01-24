class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))
        
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)

        state = [0] * numCourses
        res = []

        def dfs(pre):
            if state[pre] == 2:
                return True
            if state[pre] == 1:
                return False
            state[pre] = 1
            for course in adj[pre]:
                if not dfs(course):
                    return False

            state[pre] = 2
            res.append(pre)
            return True
        
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []
        return res[::-1]
