#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i, length in enumerate(nums):
            if i > reachable:
                break
            reachable = max(reachable, i + length)
        return reachable >= len(nums) - 1
       
# @lc code=end

