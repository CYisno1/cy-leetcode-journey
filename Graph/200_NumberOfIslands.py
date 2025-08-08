class UnionFind:
    def __init__(self, grid):
        self.count = 0 # Count the number of islands
        m, n = len(grid), len(grid[0])
        self.parent = []
        self.rank = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # Each land cell is treated as its own parent (root of its own set).
                    # This allows us to later use union(x, y) to merge connected land cells
                    # (ex. those adjacent in up/down/left/right directions).
                    self.parent.append(i * n + j) # Map 2D coordinates to a unique 1D index
                    self.count += 1 # Count this land cell as an initial island
                else:
                    self.parent.append(-1) # Water cells have no parent
                self.rank.append(0) # Initialize rank to 0 for union by rank optimization
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i]) # Recursively find the root ancestor and compress the path 
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    if r - 1 >= 0 and grid[r - 1][c] == "1": # Check up (Because unionfind use parent-- a list, so we need to change the 2-d grid into the 1-d list)
                        uf.union(r * nc + c, (r - 1) * nc + c)
                    if r + 1 < nr and grid[r + 1][c] == "1": # Check down
                        uf.union(r * nc + c, (r + 1) * nc + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1": # Check left
                        uf.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c + 1] == "1": # Check right
                        uf.union(r * nc + c, r * nc + c + 1)
        
        return uf.count

                    
    

