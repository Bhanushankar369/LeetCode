# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         m = len(s1)
#         n = len(s2)

#         if m+n < len(s3):
#             return False

#         i, j, point = 0, 0, 0
#         ipointer , jpointer = 0, 0

#         while point < len(s3):
#             while i < m and point < len(s3):
#                 if s3[point] == s1[i]:
#                     point += 1
#                     ipointer = i
#                 i+=1

#             if ipointer < m-1:
#                 i = ipointer+1

#             while j < n and point < len(s3):
#                 if s3[point] == s2[j]:
#                     point += 1
#                     jpointer = j
#                 j+=1

#             if jpointer < n-1:
#                 j = jpointer+1

#             if point >= len(s3):
#                 return True
        
#         return True if point>=len(s3) else False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # dp[i][j] = True if s3[:i+j] is formed by interleaving s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Fill dp table
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        return dp[m][n]
