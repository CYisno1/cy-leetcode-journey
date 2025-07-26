class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):

            if node is None:
                return False
            
            elif is_identical(node, subRoot):
                return True
            
            # If "tree rooted at node" was not identical.
            # Check for tree rooted at children
            return dfs(node.left) or dfs(node.right)

        def is_identical(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
        
            return (node1.val == node2.val and
                    is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right))
        
        return dfs(root)

            
