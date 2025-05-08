/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const dp = [];
    for(let i=0;i<=text1.length;i++){
        const temp = [];
        for(let j=0;j<=text2.length;j++){
            temp.push(0);
        }
        dp.push(temp);
    }
    for(let i=1;i<dp.length;i++){
        for(let j=1;j<dp[0].length;j++){
            if(text1[i-1] == text2[j-1]){
                dp[i][j] = dp[i-1][j-1]+1
            }else{
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp.at(-1).at(-1);
};