"""
Time Complexity: O(N+M), where N is a number of nodes (vertices) and M is a number of edges.
Space Complexity: O(N). This space is occupied by the visited hash map and in addition to that, space would also be occupied by the recursion stack since we are adopting a recursive approach here.
The space occupied by the recursion stack would be equal to O(H) where H is the height of the graph. Overall, the space complexity would be O(N).

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

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
        
        # Create a new node, which has the same value as nodes of the original graph.
        # We don't have cloned neighbors as of now, so [].
        # This step only copy the nodes, no links between them.
        clone_node = Node(node.val, [])

        # Visited node is key and clone node is value.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node
