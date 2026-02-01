class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def checkPalin(string):
            return string == string[::-1]

        def makePartition(ind, ds, temp):
            if ind == len(s):
                ds.append(temp[:])
                return

            for i in range(ind+1, len(s)+1):
                if checkPalin(s[ind:i]):
                    temp.append(s[ind:i])
                    makePartition(i, ds, temp)
                    temp.pop()
            
        ds = []
        makePartition(0, ds, [])

        return ds