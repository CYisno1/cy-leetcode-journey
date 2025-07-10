"""
Take [1, 1, 2, 3] as an example.
1st iteration: 1 is not in num_set, so add it to the set.
2nd iteration: 1 is in num_set, so return True.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
    
        return False
