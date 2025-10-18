#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, word: str, wordDict: list) -> bool:
    # Convert the word dictionary into a set for O(1) lookups
        n = len(word)
        maxlen = max(len(w) for w in wordDict) if wordDict else 0
        # Find the maximum word length in the dictionary
        wordSet = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        # dp[i] represents whether the first i characters can be segmented
        # Base case: empty string can always be segmented
        for i in range(1, n + 1):
            for j in range(max(0, i - maxlen), i):
            # Check all possible segmentation points
                # Only check up to max_len characters back, or to the beginning
                if word[j:i] in wordSet and dp[j]:
                    dp[i] = True
                    break
        return dp[n]      
# @lc code=end
