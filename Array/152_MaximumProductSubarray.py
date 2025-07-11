"""
Initialize res to handle edge cases where the input contains only one number or all numbers are negative.
Because the product of two negative numbers may become the largest product, we have to use the cur_max and cur_min to track the result.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_max * n
            cur_max = max(temp, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)
            
            res = max(res, cur_max)

        return res
