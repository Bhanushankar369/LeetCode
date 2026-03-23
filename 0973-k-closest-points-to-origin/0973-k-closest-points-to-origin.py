class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points):
            return points

        heap = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            heap.append((dist, (x, y)))
        
        heapq.heapify(heap)
        ans = []

        while k:
            _, (x, y) = heapq.heappop(heap)
            ans.append([x, y])
            k -= 1

        return ans
