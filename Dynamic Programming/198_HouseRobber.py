from typing import List

class Solution:
    def __init__(self):
        self.memo = []

    def rob(self, nums: List[int]) -> int:
        self.memo = [-1] * (len(nums) + 1)
        return self._rob(nums, len(nums) - 1)
    
    def _rob(self, nums, i) -> int:
        if i < 0:
            return False
        if self.memo[i] >= 0:
            return self.memo[i]
    
        result = max(self._rob(nums, i - 2) + nums[i], self._rob(nums, i - 1)) # 搶這間 → 不能搶前一間 , 不搶這間 → 看前一間的最佳解
        self.memo[i] = result
        return result
