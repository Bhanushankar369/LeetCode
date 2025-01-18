class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i=0
        ans=0
        while i<len(bank):
            for j in range(i+1, len(bank)):
                if bank[j].count('1') == 0:
                    continue
                else:
                    ans += (bank[j].count('1') * bank[i].count('1'))
                    i=j-1
                    break
            i+=1
        return ans