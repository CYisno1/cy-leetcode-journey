class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s # "hello" → "5#hello"
        return encoded

        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the position of the '#' character
            while s[j] != '#' :
                j += 1

            # Extract the length of the next word (from i up to j, not including j)
            length = int(s[i:j])

            # Extract the word of 'length' characters right after the '#'
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # Move pointer to the next encoded segment
            i = j + 1 + length
        
        return res
