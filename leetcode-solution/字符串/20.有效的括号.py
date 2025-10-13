#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
    # Stack to keep track of opening brackets
        stack = []
        
        # Map to match opening and closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from stack if there's a matching opening bracket, otherwise return False
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all the brackets were valid
        return not stack
   
# @lc code=end

