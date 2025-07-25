class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Postorder: deal with the left and right nodes first, and then the root node itself
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float("inf")

      # Post order traversal of subtree rooted at "node"
        def gainFromSubtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath    # 'maxPath' is defined in the outer function (maxPathSum). Using 'nonlocal' allows us to update the outer maxPath as we explore the tree.

            if not node:
                return 0

          # Add the gain from the left subtree. Note that if the gain is negative, we can ignore it, or count it as 0.
          # This is the reason we use `max` here.
            gainFromLeft = max(gainFromSubtree(node.left), 0)

          # Add the gain from the right subtree.
            gainFromRight = max(gainFromSubtree(node.right), 0)

            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)

          # return the max sum for a path starting at the root of subtree (每個子節點的maxsum 但最終的答案是maxPath)
            return max(gainFromLeft + node.val, gainFromRight + node.val)
        
        gainFromSubtree(root)
        return maxPath
