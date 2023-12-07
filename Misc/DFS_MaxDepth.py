class Test:
    def dfsmaxdepth(self, root):
        if not root:
            return
        left = self.dfsmaxdepth(root.left)
        right = self.dfsmaxdepth(root.right)
        return max(left, right) + 1
