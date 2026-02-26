class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(list)

        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]][0] += 1
                continue

            dic[s[i]] = [1, i] 

        for k, lst in dic.items():
            if lst[0] == 1:
                return lst[1]
        
        return -1