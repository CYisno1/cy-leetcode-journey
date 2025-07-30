class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                length = 1

                while num + length in num_set:
                    length += 1
                # Start checking from n+1, n+2, n+3... and keep going forward to see if each number
                # exists in the set, until one is not found.

                longest = max(longest, length)
        
        return longest
