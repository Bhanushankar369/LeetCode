class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        lst = defaultdict(list)
        for i in range(len(groupSizes)):
            lst[groupSizes[i]].append(i)
        ans = []
        for i in lst:
            ans.append([lst[i][j:j+i] for j in range(0, len(lst[i]), i)])
        sol = []
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                sol.append(ans[i][j])
        return sol