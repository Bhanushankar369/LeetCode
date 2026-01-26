class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        self.combinations(0, ans, temp, target, candidates)
        return ans

    def combinations(self, ind, arr, temp, target, candidates):

        if target == 0:
            arr.append(temp[:])
            return

        if target < 0 or ind == len(candidates):
            return

        target -= candidates[ind]
        temp.append(candidates[ind])
        self.combinations(ind, arr, temp, target, candidates)

        target += candidates[ind]
        temp.pop()
        self.combinations(ind+1, arr, temp, target, candidates)
