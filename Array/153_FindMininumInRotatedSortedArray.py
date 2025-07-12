"""
Binary Search, two pointers
When we find that the mid is smaller than the right, the answer(the smaller number) is on the left side, so we change the right to the mid, to search the left side.
When the mid is larger than the right, the answer is on the right side.
The algorithm stops when left and right point to the same number (the answer).
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]
