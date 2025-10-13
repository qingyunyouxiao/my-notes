#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        counts = [1, 1]
        for i in range(2, n + 1):
                count = 0
                for j in range(i):
                    count += counts[j] * counts[i - j - 1]
                counts.append(count)
        return counts[-1]
    
# @lc code=end

