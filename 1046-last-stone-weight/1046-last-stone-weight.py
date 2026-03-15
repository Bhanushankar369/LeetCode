import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if second > first:
                heapq.heappush(heap, first-second)

        heap.append(0) # If heap is empty this will add 0 and we return 0
        return abs(heap[0])