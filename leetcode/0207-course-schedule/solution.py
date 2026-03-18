from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not prerequisites[0]:
            return True
        
        courses = collections.defaultdict(list)
        inDegree = [0] * numCourses

        for u, v in prerequisites:
            courses[v].append(u)
            inDegree[u] += 1
        
        count = 0
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                
        while queue:
            cur = queue.popleft()
            count += 1
            for c in courses[cur]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)

        return count == numCourses



