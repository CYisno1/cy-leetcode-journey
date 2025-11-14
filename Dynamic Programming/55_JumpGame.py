# Bottom Down + memoization
class Solution:
    def __init__(self):
        self.memo = []
        self.nums = []
    
    def canJumpFromPosition(self, position):
        if self.memo[position] != -1:
            return self.memo[position] == 1 # if == 1, return True
        furthestJump = min(position + self.nums[position], len(self.nums) - 1)
        # how far can the position go, limit at the final num
        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition):
                self.memo[position] = 1
                return True
            # If next one is GOOD, the current one must be GOOD too.
        self.memo[position] = 0
        return False
        # Tried all position and jumps, but not work


    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        self.memo = [-1] * len(nums) 
        # -1: not yet calculated, 0: bad, cannnot reach the end, 1: good
        self.memo[-1] = 1 
        # The last position is always good.
        return self.canJumpFromPosition(0)


"""
Greedy:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
"""
