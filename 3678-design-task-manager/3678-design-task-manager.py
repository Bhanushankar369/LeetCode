import heapq
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap = []  # min-heap with (-priority, -taskId, userId, taskId)
        self.task_map = {}  # taskId -> (userId, priority)
        for u, t, p in tasks:
            heapq.heappush(self.heap, (-p, -t, u, t))
            self.task_map[t] = (u, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))
        self.task_map[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.task_map:
            return
        userId, _ = self.task_map[taskId]
        # update task_map, old entry becomes stale
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]  # lazy deletion (heap may still hold stale copy)

    def execTop(self) -> int:
        while self.heap:
            priority, negTask, userId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                curUser, curPri = self.task_map[taskId]
                if curPri == -priority:  # valid entry
                    del self.task_map[taskId]
                    return curUser
        return -1



# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()