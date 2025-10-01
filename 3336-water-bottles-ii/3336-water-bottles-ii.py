class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        Empty = 0
        BottlesDrunk = 0

        while numBottles > 0:
            Empty += numBottles
            BottlesDrunk += numBottles

            numBottles = 0

            while Empty >= numExchange:
                Empty -= numExchange
                numExchange += 1
                numBottles += 1

        return BottlesDrunk