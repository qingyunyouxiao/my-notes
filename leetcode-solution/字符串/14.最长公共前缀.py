#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first string and compare its characters with others
        for i in range(len(strs[0])):
            char = strs[0][i]  # Take the i-th character from the first string
            for string in strs:
                # If the character at the i-th position doesn't match or string is shorter
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        
        return strs[0]  # In case the first string is the LCP
        
# @lc code=end

