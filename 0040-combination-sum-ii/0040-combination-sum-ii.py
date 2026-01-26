class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        candidates.sort()

        def combinations(ind, ans, temp, target, candidates):
            if target == 0:
                ans.append(temp[:])
                return

            if target < 0 or ind == len(candidates):
                return

            for i in range(ind, len(candidates)):
                if i>ind and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target:
                    break

                temp.append(candidates[i])
                combinations(i+1, ans, temp, target-candidates[i], candidates)
                temp.pop()
        
        combinations(0, ans, [], target, candidates)
        return ans