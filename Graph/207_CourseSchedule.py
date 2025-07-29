# Topological Sort/ Kahn's Algorithm

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Create an array indegree of length n where indegree[x] stores the incoming degree (number of edges entering node x)
        indegree = [0] * numCourses
        # Create an adjacency list adj in which adj[x] contains all the nodes with an incoming edge from node x
        adj = [[] for _ in range(numCourses)]

        # We create this adjacency list by iterating over prerequisites
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        nodesVisited = 0
        # While the queue is not empty; Dequeue the first node from the queue.
        # Increment nodesVisited by 1.
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return nodesVisited == numCourses
        # If the number of nodes visited is less than the total number of nodes, i.e., nodesVisited < n we return false as there must be a cycle. Otherwise, if nodesVisited == numCourses, we return true.
        

    
