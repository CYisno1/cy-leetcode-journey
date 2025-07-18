# How to think: how to set the sliding window left and right boreder -> in What situation we have to change the border and update the answer

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Count the required frequency of each character in t
        dict_t = Counter(t)

        # Number of unique characters in t that must be present in the window
        required = len(dict_t)

        # Left and right pointers of the sliding window
        l, r = 0, 0
        
        # `formed` keeps track of how many unique characters in t
        # have their desired frequency satisfied in the current window
        formed = 0

        # Frequency of each character in the current window
        window_counts = {}

        # Result tuple: (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
        
            # If the current character is required, and its frequency matches
            # the requirement in t, we count it as "formed"
            if (
                character in dict_t
                and window_counts[character] == dict_t[character]
            ):
                formed += 1
        
            # Try to shrink the window from the left
            # Only do this if all required characters are currently satisfied
            while l <= r and formed == required:
                character = s[l]

                # Update result if current window is smaller than the previous best
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
            
                # Remove character at position l from the window
                window_counts[character] -= 1
                if (
                    character in dict_t
                    and window_counts[character] < dict_t[character]
                ):
                    formed -= 1
            
                l += 1
        
            # Expand the window to the right
            r += 1

        # Return the smallest window substring, or empty if not found
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
