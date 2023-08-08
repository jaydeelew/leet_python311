class Solution:
    def simplify_path(self, path: str) -> str:
        split = path.split("/")
        stack = []
        omit_set = {"", ".", ".."}
        for s in split:
            if stack and s == "..":
                stack.pop()
            elif s not in omit_set:
                stack.append(s)
        path_str = []
        for c in stack:
            path_str.append("/")
            path_str.append(c)
        if not path_str:
            path_str.append("/")
        return "".join(path_str)


sol = Solution()
# path = "/home/"  # Output: "/home"
# path = "/../"  # Output: "/"
# path = "/home//foo/"  # "/home/foo"
# path = "home"  # Output: "/home"
path = "/a/./b/../../c/"  # Output: "/c" (Any two directories are separated by a single slash '/')
print(sol.simplify_path(path))
