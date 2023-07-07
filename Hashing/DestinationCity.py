# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        paths_dict = dict(paths)
        # for city1, city2 in paths:
        #     paths_dict[city1] = city2

        for key in paths_dict:
            if paths_dict[key] not in paths_dict:  # if the dictionary value is not a key in the dictionary
                return paths_dict[key]
        return "no result"


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]  # returns: Sao Paulo
# paths = [["B", "C"], ["D", "B"], ["C", "A"]]  # returns A
sol = Solution()
print(sol.destCity(paths))
