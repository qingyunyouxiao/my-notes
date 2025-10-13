#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a set to store characters of the current window
        char_set = set()
        left = 0  # Left pointer for the sliding window
        max_len = 0  # To track the maximum length of the substring

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character at right pointer is already in the window, shrink from the left
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the leftmost character from the set
                left += 1  # Move the left pointer to the right

            # Add the new character to the set
            char_set.add(s[right])

            # Update the maximum length
            max_len = max(max_len, right - left + 1)

        return max_len   

# @lc code=end

