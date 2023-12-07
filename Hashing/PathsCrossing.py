# 1496. Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west,
# respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited.
# Return false otherwise.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = set()
        points.add((0, 0))
        x = y = 0
        for c in path:
            if c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            elif c == "W":
                x -= 1

            if (x, y) in points:
                return True

            points.add((x, y))

        return False


# path = "NES"
# Output: False

path = "NESWW"
# Output: True

sol = Solution()
print(sol.isPathCrossing(path))
