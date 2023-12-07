# 71. Given a string path, which is an absolute path (starting with a slash '/') to a file or directory
# in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory,
# a double period '..' refers to the directory up a level,
# and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
# For this problem, any other format of periods such as '...' are treated as file/directory names.
# The canonical path should have the following format:
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root
# directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path


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


path = "/a/./b/../../c/"
# Output: "/c"

# path = "/home/"
# Output: "/home"

# path = "/../"
# Output: "/"

# path = "/home//foo/"
# Output: "/home/foo"

# path = "home"
# Output: "/home"

sol = Solution()
print(sol.simplify_path(path))
