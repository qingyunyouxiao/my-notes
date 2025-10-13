#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the shorter array for better binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # Number of elements that should be in the left half
        
        # Perform binary search on nums1
        left, right = 0, m
        
        while left < right:
            i = left + (right - left + 1) // 2  # Partition point in nums1
            j = total_left - i  # Partition point in nums2
            
            if nums1[i - 1] > nums2[j]:
                # Max value in left half of nums1 > min value in right half of nums2
                # Need to reduce number of elements in left half of nums1
                right = i - 1
            else:
                left = i
        
        i = left
        j = total_left - i
        
        # Handle edge cases
        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]
        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]
        
        # Calculate median
        if (m + n) % 2 == 1:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
               
# @lc code=end

