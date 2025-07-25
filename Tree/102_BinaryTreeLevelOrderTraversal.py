class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node: TreeNode, level: int) -> None:

          # If we reach a new level for the first time, add an empty list to store node values at this level.
          # Ex. if we're currently processing level 2 but the length of levels is only 2, it means we've only created lists for level 0 and level 1 so far.
            if len(levels) == level:
                levels.append([])

          # Add the current node's value to the corresponding level list
            levels[level].append(node.val)

          # Recursively process the left and right children, increasing the level by 1
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        
        helper(root, 0)
        return levels
