# Union Find

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # Check whether i's a valid tree
            return False
        parent = list(range(n))


        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        for u, v in edges:
            if find(u) == find(v): # Check if there is cycle
                return False
            union(u, v)
        
        return True
