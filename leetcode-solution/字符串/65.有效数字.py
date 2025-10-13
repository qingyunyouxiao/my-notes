#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        numSeen = False
        dotSeen = False
        eSeen = False
        numAfterE = True

        for i, c in enumerate(s):
            if c.isdigit():
                numSeen = True
                if eSeen:
                    numAfterE = True
            elif c in ['+', '-']:
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif c == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif c in ['e', 'E']:
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numAfterE = False  # need at least one digit after e
            else:
                return False

        return numSeen and numAfterE
    
# @lc code=end

