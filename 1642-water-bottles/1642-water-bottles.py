class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles

        while numBottles >= numExchange:
            to_bottles = numBottles // numExchange
            result += to_bottles

            numBottles %= numExchange
            numBottles += to_bottles
        
        return result