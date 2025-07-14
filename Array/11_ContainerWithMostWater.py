"""
Use two pointers left and right, and maxArea to keep track of the maxArea found.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            width = right - left
            currentArea = min(height[left], height[right]) * width
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
