#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # 1. Trim leading spaces
        if not s:
            return 0

        # 2. Check sign
        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            i += 1

        # 3. Convert digits
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        num *= sign

        # 4. Clamp
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
       
# @lc code=end

