#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Minimum is in the left half or is mid itself
                right = mid
            else:
                # nums[mid] == nums[right], uncertain, shrink right boundary
                right -= 1
        
        return nums[left]
        
# @lc code=end

