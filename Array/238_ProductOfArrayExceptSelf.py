"""
First initialize two arrays to calculate the left side (prefix) and the right side (suffix) of nums list. They are composed of 1 wich will not influence the result.
We calculate the product of left side except for the current element, and we do the same thing on the right side, and then mutiply the product of the two sides.
"""

class Solution:
     def productExceptSelf(self, nums: List[int]) -> List[int]:
         n = len(nums)
         pre_arr = [1] * n
         suff_arr = [1] * n
         res = [0] * n

         for i in range(1,n):
             pre_arr[i] = nums[i-1] * pre_arr[i-1]
         for j in range(n-2, -1, -1):
             suff_arr[j] = nums[j+1] * suff_arr[j+1]
         for i in range(n):
             res[i] = pre_arr[i] * suff_arr[i]
         return res

