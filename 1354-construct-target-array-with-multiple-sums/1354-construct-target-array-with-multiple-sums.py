class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-t for t in target]
        total = sum(target)
        heapq.heapify(heap)

        while -heap[0] > 1:
            maxi = -heapq.heappop(heap)
            rest = total - maxi

            if rest == 1:
                return True

            if rest == 0:
                return False

            rem = maxi % rest # Useful for the cases like [1,1000000000]
            if rem == 0 or rem >= maxi:
                return False

            heapq.heappush(heap, -rem)
            total = rest + rem
 
        return True