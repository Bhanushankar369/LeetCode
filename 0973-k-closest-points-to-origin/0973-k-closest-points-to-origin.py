class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points):
            return points

        heap = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for _, point in heap:
            ans.append(point)
        
        return ans