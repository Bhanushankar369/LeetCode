class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ds=[]
        ans=[]
        def recurs(ind, target, candidates, ds, ans):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                recurs(ind, target-candidates[ind], candidates, ds, ans)
                ds.pop()
            recurs(ind+1, target, candidates, ds, ans)
        recurs(0, target, candidates, ds, ans)
        return ans