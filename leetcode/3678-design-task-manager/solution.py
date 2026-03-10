class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.mp = {}
        self.heap = []
        for uid, tid, p in tasks:
            self.mp[tid] = [uid, p]
            self.heap.append((-p, -tid))
        heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mp[taskId] = [userId, priority]
        heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.mp[taskId][1] = newPriority
        heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.mp[taskId]

    def execTop(self) -> int:
        while self.heap:
            p, tid = heappop(self.heap)
            p, tid = -p, -tid
            if tid in self.mp and self.mp[tid][1] == p:
                uid = self.mp[tid][0]
                del self.mp[tid]
                return uid
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
