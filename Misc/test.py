class Test:
    def dfsmaxdepth(self, root):
        if not root:
            return
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return max(left, right) + 1
