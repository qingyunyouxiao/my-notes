#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for index in range(1,len(dp[0])):
            if p[index-1] == '*':
                dp[0][index] = dp[0][index-1]

        for index_i in range(1, len(dp)):
            for index_j in range(1, len(dp[0])):
                if s[index_i - 1] == p[index_j - 1] or p[index_j - 1] == '?':
                    dp[index_i][index_j] = dp[index_i-1][index_j-1]
                elif p[index_j-1] == '*':
                    dp[index_i][index_j] = dp[index_i][index_j-1] or dp[index_i-1][index_j]
                else:
                    dp[index_i][index_j] = False
        return dp[len(s)][len(p)]

# @lc code=end

