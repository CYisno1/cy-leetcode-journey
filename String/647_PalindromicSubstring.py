class Solution:
    def countSubstrings(self, s: str) -> int:

      # Expand around the center and count how many palindromic substrings exist
        def expand_around_center(left: int, right: int):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1   # Found a valid palindromic substring
                left -= 1
                right += 1
            return count
        
        result = 0
        for i in range(len(s)):
          
          # Try to expand for odd-length palindromes centered at s[i]
            result += expand_around_center(i, i)
          # Try to expand for even-length palindromes centered between s[i] and s[i+1]
            result += expand_around_center(i, i + 1)
        
        return result
