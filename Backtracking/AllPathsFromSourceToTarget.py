# 797. Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
# find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
# (i.e., there is a directed edge from node i to node graph[i][j]).


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def backtrack(curr_path: list[int], node: int):
            # if current path array ends with the terminating node
            if curr_path[-1] == len(graph) - 1:
                ans.append(curr_path.copy())
                return

            for neighbor in graph[node]:
                if neighbor not in curr_path:
                    curr_path.append(neighbor)
                    # neighbor becomes the next node to look for more neighbors in the graph
                    backtrack(curr_path, neighbor)
                    curr_path.pop()

        ans = []
        backtrack([0], 0)
        return ans


sol = Solution()

# graph = [[1, 2], [3], [3], []]
# Output: [[0, 1, 3], [0, 2, 3]]

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
# Output: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]

print(sol.allPathsSourceTarget(graph))
