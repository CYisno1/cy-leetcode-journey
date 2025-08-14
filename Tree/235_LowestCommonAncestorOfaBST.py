# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:       
        # Value of current node/parent node.
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point
        else:
            return root

        
