#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtracking(S, left, right):
            if len(S) == 2*n:
                result.append(S)
                return 

            if left < n:
                backtracking(S+'(', left+1, right)

            if right < left:
                backtracking(S+')', left, right+1)

        backtracking('', 0, 0)
        return result
  
# @lc code=end

