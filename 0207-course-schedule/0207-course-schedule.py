class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0]*numCourses

        map = defaultdict(list)
        for u, v in prerequisites:
            map[u].append(v)
            indeg[v] += 1

        dq = deque([])
        for i in range(numCourses):
            if indeg[i] == 0:
                dq.append(i)

        count = 0
        while dq:
            node = dq.popleft()
            count += 1
            for nei in map[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    dq.append(nei)

        return count == numCourses