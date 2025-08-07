from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], src: int, dst: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        prob = [0.0] * n
        prob[src] = 1.0
        heap = [(-1.0, src)]

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -curr_prob

            if node == dst:
                return curr_prob

            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0
