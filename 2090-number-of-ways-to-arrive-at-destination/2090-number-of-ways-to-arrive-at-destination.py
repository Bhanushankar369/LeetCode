class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        map = defaultdict(list)
        for u, v, w in roads:
            map[u].append((v, w))
            map[v].append((u, w))

        ways = [0]*n
        ways[0] = 1

        target = n-1

        dist = [float('inf')]*n
        dist[0] = 0

        heap = []
        heapq.heappush(heap, (0, 0))

        while heap:
            dis, node = heapq.heappop(heap)
            for nei, wei in map[node]:
                if dist[nei] > dis + wei:
                    dist[nei] = dis+wei
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (dis+wei, nei))

                elif dist[nei] == dis + wei:
                    ways[nei] = (ways[nei] + ways[node]) % (10**9 + 7)

        return ways[target] % (10**9 + 7)