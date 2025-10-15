/*
 * @lc app=leetcode.cn id=139 lang=typescript
 *
 * [139] 单词拆分
 */

// @lc code=start
function wordBreak(word: string, wordDict: string[]): boolean {
  const n = word.length;
  const maxlen = wordDict.reduce((max, word) => Math.max(max, word.length), 0);
  const wordSet = new Set(wordDict);
  const dp = new Array(n + 1).fill(false);
  dp[0] = true;

  for (let i = 1; i <= n; i++) {
    for (let j = Math.max(0, i - maxlen); j < i; j++) {
      if (wordSet.has(word.slice(j, i)) && dp[j]) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[n];
};
// @lc code=end
