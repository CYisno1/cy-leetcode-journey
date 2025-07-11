"""
First we initialize maxSum and currentSum. maxSum represents the maximum sum encountered so far and is initially set to the minimum possible integer value to ensure that any valid subarray sum will be greater than it.
currentSum represents the sum of the current subarray.

If the currentSum is larger than maxSum, we update the maxSum.

If the current sum becomes negative, we reset it as 0 and start a new subarray.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum
