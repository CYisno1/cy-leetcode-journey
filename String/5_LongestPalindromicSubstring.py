"""
1. Check if the input string s is empty. If it is, return an empty string, as there can be no palindromic substring in an empty string.

2. Define a helper function expand_around_center that takes three arguments: the input string s, and two indices left and right. This function is responsible for expanding the palindrome around the center indices and returns the length of the palindrome.
(Why right - left - 1? left and right pointer always overrun and stop at max length in current iteration + 1, so we need to subtract -1 from right - left.)

3. Initialize start and end variables to 0. These variables will be used to keep track of the indices of the longest palindromic substring found so far.

4. Iterate through each character of the input string s using a for loop.

5. Inside the loop, call the expand_around_center function twice: once with i as the center for an odd length palindrome and once with i and i + 1 as the center for an even length palindrome.

6. Calculate the length of the palindrome for both cases (odd and even) and store them in the odd and even variables.

7. Calculate the maximum of the lengths of the two palindromes and store it in the max_len variable.

8. Check if the max_len is greater than the length of the current longest palindromic substring (end - start). If it is, update the start and end variables to include the new longest palindromic substring. The new start is set to i - (max_len - 1) // 2, and the new end is set to i + max_len // 2.

9. Continue the loop until all characters in the input string have been processed.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        

        start = 0
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end+1]
