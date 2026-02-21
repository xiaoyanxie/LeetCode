from collections import defaultdict
import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        """
        userId, taskId, priority
        """

        # order by priority, taskId DESC
        self.queue = []
        self.index = defaultdict(Tuple[int, int])
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.queue, (-priority, -taskId, userId))
        self.index[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.index[taskId]
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        if taskId in self.index:
            del self.index[taskId]

    def execTop(self) -> int:
        while self.queue:
            priority, taskId, userId = heapq.heappop(self.queue)
            priority, taskId = abs(priority), abs(taskId)
            if taskId in self.index and self.index[taskId] == (userId, priority):
                self.rmv(taskId)
                return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
