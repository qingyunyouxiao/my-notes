#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        # initialize the array
        heights = [0] * cols
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            stack = []
            extended_heights = heights + [0]
            
            for j in range(len(extended_heights)):
                while stack and extended_heights[j] < extended_heights[stack[-1]]:
                    h = extended_heights[stack.pop()]
                    # If the stack is empty, the width is j
                    # otherwise, it is j - stack[-1] - 1
                    w = j if not stack else j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)
        
        return max_area
# @lc code=end

