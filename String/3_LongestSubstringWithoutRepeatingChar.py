"""
Sliding Window!
i is the left boundary of the sliding window; j is the right boundary of the sliding window.
If current character has appeared before, move the left pointer to the right of the previous occurrence (to avoid repeating characters)>> i = j + 1
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        charToNextIndex = {} # Dictionary to store the index+1 of each character's last occurrence

        i = 0
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)
            
            ans = max(ans, j - i + 1) # Update the answer with the length of the current window
            charToNextIndex[s[j]] = j + 1 # Store the index+1 of the current character
        
        return ans
