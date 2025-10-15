#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# 
class Solution(object):
    def maxPathSum(self, root):
        def dfs(node):
            if not node:
                return (float("-inf"), 0)
            max_left, curr_left = dfs(node.left)
            max_right, curr_right = dfs(node.right)
            return (max(max_left, max_right, node.val+max(curr_left, 0)+max(curr_right, 0)),
                    node.val+max(curr_left, curr_right, 0))
        
        return dfs(root)[0]     
# @lc code=end
