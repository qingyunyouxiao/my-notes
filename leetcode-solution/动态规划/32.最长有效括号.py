#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, result = [-1], 0
        for index in range(len(s)):
            if s[index] == '(':
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    result = max(result, index - stack[-1])
        return result   
    
# @lc code=end

