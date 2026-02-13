from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # classic topsort
        graph = defaultdict(set) # {0: [1], 1: [0]}
        indegree = { i: 0 for i in range(numCourses) } # {0: 1, 1: 1, 2: 0}
        for second, first in prerequisites: # 0, 1
            indegree[second] += 1
            graph[first].add(second)
        
        queue = deque([ i for i in indegree if indegree[i] == 0 ]) # []
        schedule = [] # [2]
        while queue:
            course = queue.popleft()
            schedule.append(course)
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return len(schedule) == numCourses
