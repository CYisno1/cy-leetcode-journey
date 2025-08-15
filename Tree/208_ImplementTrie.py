class Trie:
    class Node:
        def __init__(self):
            self.links = [None] * 26  # A list to store the 26 nodes (a ~ z)
            self.is_end = False       # Mark if it's the end of a complete word
    
    def __init__(self):
        self.root = self.Node()  # Build the root node
    
    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            index = ord(char) - ord('a') # index for a~z in the self.links list
            if current_node.links[index] is None:         # (Ex. car) if we can't find c in the list,
                current_node.links[index] = self.Node()   # make a new node for it
            current_node = current_node.links[index]      # current_node moves to the node we just create
        
        current_node.is_end = True
    
    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            index = ord(char) - ord('a')
            current_node = current_node.links[index]
            if current_node is None:
                return False
        return current_node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            current_node = current_node.links[index]
            if current_node is None:
                return False
        return True
    
