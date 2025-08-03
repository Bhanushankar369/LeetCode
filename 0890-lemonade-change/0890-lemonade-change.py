class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10:
                if fives < 1:
                    return False
                
                fives -= 1
                tens += 1

            else:
                if tens < 1:
                    if fives < 3:
                        return False
                    else:
                        fives -= 3
                        twenties += 1
                
                else:
                    if fives < 1:
                        return False
                    
                    tens -= 1
                    fives -= 1
                    twenties += 1

        return True
                
