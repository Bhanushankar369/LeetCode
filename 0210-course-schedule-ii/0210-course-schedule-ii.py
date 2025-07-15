class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0]*numCourses

        map = defaultdict(list)
        for u, v in prerequisites:
            map[u].append(v)
            indeg[v] += 1

        dq = deque([])
        for i in range(numCourses):
            if indeg[i] == 0:
                dq.append(i)

        stack = []
        while dq:
            node = dq.popleft()
            stack.append(node)
            for nei in map[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    dq.append(nei)

        result = []
        for i in range(len(stack)):
            result.append(stack.pop())

        if len(result) == numCourses:
            return result
        
        return []