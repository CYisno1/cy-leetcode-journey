class Solution:
    def __init__(self):
        self.memo = []

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self._rob_linear(nums, 0, n - 2), self._rob_linear(nums, 1, n - 1))
                   # Case1: Include 1st House (no last House)  # Case2: Include last House (no 1st House)
    
    def _rob_linear(self, nums, start, end):
        # base case: only one house left
        if start == end:
            return nums[start]
        
        self.memo = [-1] * len(nums)
        return self._rob(nums, end, start)

    
    def _rob(self, nums, i, start) -> int:
        if i < start:
            return 0
        if self.memo[i] >= 0:
            return self.memo[i]
        
        result = max(self._rob(nums, i - 2, start) + nums[i], self._rob(nums, i - 1, start))
        self.memo[i] = result
        return result
