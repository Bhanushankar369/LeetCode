/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    const dp = [];
    for(let k=0;k<nums.length;k++){
        dp.push(1);
    }
    for(let i=0;i<nums.length;i++){
        for(let j=0;j<i;j++){
            if(nums[i] > nums[j]){
                dp[i] = Math.max(dp[j]+1, dp[i]);
            }
        }
    }
    ans = 0
    for(let key in dp){
        if (ans < dp[key]){
            ans = dp[key];
        }
    }
    return ans
};