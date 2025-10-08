class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        result = [0]*len(spells)

        for i in range(len(spells)):
            left = 0
            right = len(potions)
            num = spells[i]

            paired_ind = -1

            while left < right:
                mid = (left+right)//2
                if num*potions[mid] >= success:
                    paired_ind = mid
                    right = mid
                else:
                    left = mid+1
                
            if paired_ind == -1:
                result[i] = 0
            else:
                result[i] = len(potions) - paired_ind

        return result