from typing import Optional

class Solution:

    def __init__(self):
        # Dictionary to save the visited node (key) and it's respective clone (value).
        # This helps to avoid cycles.
        # As an object of the Solution class, every recursion can use it.
        self.visited = {}
    
    # node: Optional["Node"] represents it may be a node or none
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        
        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]
        
        # Create a clone for the given node.
        # We don't have cloned neighbors as of now, so [].
        clone_node = Node(node.val, [])

        # Visited node is key and clone node is value.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node
