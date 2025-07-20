class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_char = []

        for c in s:
            if c.isalnum(): # Only keep alphanumeric characters (letters and digits).
                            # `isalnum()` is short for "is alphanumeric".
                clean_char.append(c.lower()) # Convert each remaining letter to lowercase (digits are unaffected).
        
        s = ''.join(clean_char) # Get the clean lower-cased, no-space string
        
        # Two pointers
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
