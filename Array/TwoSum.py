"""
The first solution that came to my mind is brute force, which loops through each element x and checks whether there is a target - x. However, this leads to a time complexity of O(n²).

A more efficient approach is using a HashMap. In the first iteration, we add each element's value as the key and its index as the value in the HashMap. Then, in the second iteration, we check if the complement target - current element exists in the HashMap.
Also, we have to ensure that the current element and the complement are not the same element. This solution trades space for speed.

TC: O(n), SC: O(n)
Because the HashMap reduces the search time to O(1), the overall time complexity is O(n) for the iteration, and the space complexity is O(n) for storing n elements.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
