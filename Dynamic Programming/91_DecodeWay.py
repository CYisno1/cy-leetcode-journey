class Solution:

    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int: # func: R()
        # Choice 2
        # Reach the end of the string >> return 1
        if index == len(s):
            return 1
        
        # The string starts with a zero, it cannot be decoded
        if s[index] == '0':
            return 0
        
        # Choice 1
        # Reach the last number in the string
        if index == len(s) - 1:
            return 1
        
        # Choice 1: Only decode 1 number (s[index]), and ask how many solution left for R(index+1)
        answer = self.recursiveWithMemo(index + 1, s) 
        # Choice 2: Decode 2 numbers, and ask how many solution left for R(index+2)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)
        
        return answer
    
    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)
        
