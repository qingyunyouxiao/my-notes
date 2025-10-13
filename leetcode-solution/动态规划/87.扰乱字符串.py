#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # dp[i][j][l]
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                for j in range(n - l + 1):
                    for k in range(1, l):
                        # No swap
                        if dp[i][j][k] and dp[i + k][j + k][l - k]:
                            dp[i][j][l] = True
                            break
                        # Swap
                        if dp[i][j + l - k][k] and dp[i + k][j][l - k]:
                            dp[i][j][l] = True
                            break
        return dp[0][0][n]
    
# @lc code=end

