# Sliding Window + Binary Search

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We are doing binary search over the possible substring lengths.
        # Goal: Find the longest length L such that there exists a substring
        # of length L that can be made all the same character with at most k replacements.

        lo = 1  # lower bound (we can always make a valid substring of length 1)
        hi = len(s) + 1  # upper bound (invalid value - exclusive)

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2  # Try a candidate substring length

            # ❓ Check if there's any substring of length `mid`
            #    that can be made valid (all same character) with ≤ k replacements
            if self.__can_make_valid_substring(s, mid, k):
                # If possible, try to go longer
                lo = mid
            else:
                # If not possible, try shorter lengths
                hi = mid

        # Final answer is the longest valid length we found
        return lo

    def __can_make_valid_substring(self, s: str, substring_length: int, k: int) -> bool:
        # Use a sliding window of size `substring_length` to scan the string
        # We check whether we can turn the whole window into the same character
        # using at most `k` replacements.

        freq_map = {}        # Keeps track of character counts in the window
        max_frequency = 0    # Stores the frequency of the most common character in the current window
        start = 0            # Left boundary of the sliding window

        for end in range(len(s)):
            # Expand the window by adding character s[end]
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            # 🔍 Only s[end] changed, so it's the only one that might become the new max.
            # No need to scan the whole dict — this keeps time complexity O(n)
            max_frequency = max(max_frequency, freq_map[s[end]])

            # If the window size exceeds the target `substring_length`, we shrink from the left
            if end + 1 - start > substring_length:
                # Before shrinking, decrease the count of the character that is sliding out
                freq_map[s[start]] -= 1
                start += 1

            # 🧠 This is the core validity condition:
            # Can we make the whole window consist of one repeated character by changing ≤ k characters?
            # - max_frequency: the count of the most frequent character in the current window
            # - substring_length - max_frequency: number of characters we need to change
            if substring_length - max_frequency <= k:
                return True  # Found a valid window

        # No valid substring of this length exists
        return False
