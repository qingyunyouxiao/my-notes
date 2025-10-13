#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0           
        base = 1          
        high = n // 10    
        cur = n % 10      
        low = 0           

        while high != 0 or cur != 0:
            if cur == 0:
                # 
                res += high * base
            elif cur == 1:
                # 
                res += high * base + (low + 1)
            else:
                #
                res += (high + 1) * base

            low += cur * base
            cur = high % 10
            high //= 10
            base *= 10
        
        return res
    
# @lc code=end

