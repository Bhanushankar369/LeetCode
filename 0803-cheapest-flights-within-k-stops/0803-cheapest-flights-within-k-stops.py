from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        map = defaultdict(list)
        for u, v, price in flights:
            map[u].append((v, price))
        
        visited = set()
        dist = [float('inf')]*n
        dist[src] = 0

        heap = []
        heapq.heappush(heap, (0, src, 0))

        while heap:
            stops, pos, cost = heapq.heappop(heap)
            if pos == dst and stops < k+1:
                if dist[pos] > cost:
                    dist[pos] = cost
            for nei, price in map[pos]:
                if stops+1 > k+1:
                    continue

                if dist[nei] > cost+price:
                    dist[nei] = cost+price
                    heapq.heappush(heap, (stops+1, nei, cost+price))

        return dist[dst] if dist[dst] != float('inf') else -1