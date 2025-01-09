# 1436. Destination City
# You are given the array paths, where paths[i] = [cityA_i, cityB_i] means there
# exists a direct path going from cityA_i to cityB_i.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        paths_dict = dict(paths)

        for key in paths_dict:
            # if dictionary value is not a key in dictionary
            if paths_dict[key] not in paths_dict:
                return paths_dict[key]
        return "no result"


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
# Output: Sao Paulo

# paths = [["B", "C"], ["D", "B"], ["C", "A"]]
# # Output: A

sol = Solution()
print(sol.destCity(paths))
