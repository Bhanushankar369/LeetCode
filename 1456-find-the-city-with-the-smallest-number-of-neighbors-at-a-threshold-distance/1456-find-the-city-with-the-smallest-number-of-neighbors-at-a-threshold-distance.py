val = 10**8
class Solution:
    def findTheCity(self, num: int, edges: List[List[int]], distanceThreshold: int) -> int:
        map = defaultdict(list)
        for u, v, w in edges:
            map[u].append((v, w))
            map[v].append((u, w))

        def dijkstra(src):
            dist = [float('inf')]*num
            dist[src] = 0

            heap =  []
            heapq.heappush(heap, (0, src))

            while heap:
                distance, node = heapq.heappop(heap)
                for nei, wei in map[node]:
                    if dist[nei] > distance + wei:
                        dist[nei] = distance + wei
                        heapq.heappush(heap, (distance+wei, nei))
            return dist

        result_node = -1
        result_neis = float('inf')

        for i in range(num):
            arr = dijkstra(i)
            count = 0
            for n in arr:
                if n <= distanceThreshold:
                    count += 1
            
            if result_neis >= count:
                result_neis = count
                result_node = i

        return result_node

            