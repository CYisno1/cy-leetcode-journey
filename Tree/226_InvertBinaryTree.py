class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
      # This returns the root of the flipped subtree, so that the previous recursion call can continue connecting the results together. (這裡回傳的是已經翻轉完成的這棵子樹的根節點，這樣上一層的遞迴可以繼續把結果「接起來」。)

