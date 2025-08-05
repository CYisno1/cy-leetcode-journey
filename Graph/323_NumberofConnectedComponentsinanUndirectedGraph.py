from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Initialize parent list. Each node is its own parent initially.
        p = list(range(n))

        # Step 2: Define find function with path compression.
        # It returns the root of node v, and flattens the tree structure along the way.
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])  # Path compression: make all nodes point directly to the root.
            return p[v]

        # Step 3: For each edge, union the two connected nodes.
        # We connect the roots of the two nodes.
        for v, w in edges:
            p[find(v)] = find(w)

        # Step 4: Count the number of unique root parent.
        # Breakdown of the following line:
        # - map(find, p): applies find() to each node index (0 to n-1), returning their root parent
        # - set(...): removes duplicates — only distinct roots are kept
        # - len(...): counts how many distinct components we have
        return len(set(map(find, p)))

        """
        Example:
        Input:
            n = 5
            edges = [[0, 1], [1, 2], [3, 4]]

        Step-by-step:

        Initial parent list:
            p = [0, 1, 2, 3, 4]

        Processing edge [0, 1]:
            find(0) = 0
            find(1) = 1
            → connect 0 to 1 → p[0] = 1
            p = [1, 1, 2, 3, 4]

        Processing edge [1, 2]:
            find(1) = 1
            find(2) = 2
            → connect 1 to 2 → p[1] = 2
            p = [1, 2, 2, 3, 4]

        Processing edge [3, 4]:
            find(3) = 3
            find(4) = 4
            → connect 3 to 4 → p[3] = 4
            p = [1, 2, 2, 4, 4]

        Now apply find() to all nodes to compress paths:

            find(0) → p[0] = find(1) = find(2) = 2
            find(1) → p[1] = find(2) = 2
            find(2) → 2
            find(3) → p[3] = find(4) = 4
            find(4) → 4

            After compression:
                p = [2, 2, 2, 4, 4]

        Unique roots = {2, 4}
        → Number of connected components = 2
        """
