class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(ranks, cars, min_cars):
            import math
            count=0
            for i in ranks:
                c2 = min_cars//i
                c = int(math.sqrt(c2))
                count += c
            return count >= cars


        l, r = 0, 1e14
        while l<r:
            mid = (l+r)//2
            if can_repair(ranks, cars, mid):
                r = mid
            else:
                l = mid+1
        return int(l)