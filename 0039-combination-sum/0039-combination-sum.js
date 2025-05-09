/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const ds = [];
    const ans = [];
    function recurs(ind, candidates, target, ds, ans){
        if(ind == candidates.length){
            if (target == 0){
                ans.push(ds.slice(0,ds.length));
            }
            return;
        }
        if(candidates[ind] <= target){
            ds.push(candidates[ind]);
            recurs(ind, candidates, target-candidates[ind], ds, ans);
            ds.pop();
        }
        recurs(ind+1, candidates, target, ds, ans);
    }
    recurs(0, candidates, target, ds, ans);
    return ans;
};