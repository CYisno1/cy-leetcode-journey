# Inorder: left -> root -> right, so to check if this tree is a validate tre, we also follow this sequence

import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(root):  # root record the current node
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            
            self.prev = root.val  # Update the previous to the current (root)node we just deal with
            return inorder(root.right)
        
        self.prev = -math.inf  # Initialize the self.prev as the smallest number so the first node can pass the iterations
        return inorder(root)
