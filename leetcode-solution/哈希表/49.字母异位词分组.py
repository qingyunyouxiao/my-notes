#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_groups[sorted_s].append(s)
        
        return list(anagram_groups.values())
    
# @lc code=end

