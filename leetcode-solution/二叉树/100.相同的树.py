#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None -> same
        if not p and not q:
            return True
        # If one is None but not the other -> not same
        if not p or not q:
            return False
        # If values differ -> not same
        if p.val != q.val:
            return False
        
        # Recurse for left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# @lc code=end

