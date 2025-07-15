class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        map = defaultdict(list)
        indeg = [0]*n

        for i in range(n):
            for j in graph[i]:
                map[j].append(i)
                indeg[i] += 1

        dq = deque([])
        for i in range(n):
            if indeg[i] == 0:
                dq.append(i)

        safe = []

        while dq:
            node = dq.popleft()
            safe.append(node)
            for nei in map[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    dq.append(nei)

        return sorted(safe)
        