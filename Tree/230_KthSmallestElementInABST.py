# Inorder Traversal will go from the smallest to the largest node in a BST

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(r: Optional[TreeNode], result: List[int]):
            if not r:
                return
            
            inorder(r.left, result)
            result.append(r.val)
            return inorder(r.right, result)
        
        value = [] # A list to place the output/ result of inorder traversal
        inorder(root, value)
        return value[k - 1]
