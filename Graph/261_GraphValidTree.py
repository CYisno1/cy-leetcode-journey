# Union Find

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty: # Cycle, return False
                return False
            parent[rootx] = rooty
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        return True
