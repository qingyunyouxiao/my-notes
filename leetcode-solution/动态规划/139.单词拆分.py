#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, word: str, wordDict: list) -> bool:
        n = len(word)
        maxlen = max(len(w) for w in wordDict) if wordDict else 0
        wordSet = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(max(0, i - maxlen), i):
                if word[j:i] in wordSet and dp[j]:
                    dp[i] = True
                    break
        return dp[n]      
# @lc code=end
