# 841. Keys and Rooms
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
# Your goal is to visit all the rooms.
# When you visit a room, you may find a set of distinct keys in it.
# Each key has a number on it, denoting which room it unlocks,
# and you can take all of them with you to unlock the other rooms.
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
# return true if you can visit all the rooms, or false otherwise


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        def dfs(node):
            for neighbor in rooms[node]:
                # if we cannot reach an index in adjacency list, rooms, starting w/ room[0] and calling neighbors recursively,
                # we will never add the "key" for that index to seen, and therefore len(seen) < len(rooms)
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = {0}
        dfs(0)
        return len(seen) == len(rooms)

    def canVisitAllRooms_Iterative(self, rooms: list[list[int]]) -> bool:
        seen = {0}
        # stack = [rooms[0]]  # placing the entire list of keys on the stack uses more memory
        stack = [0]
        while stack:
            room_index = stack.pop()
            # for key in room:  # this works with stack = [rooms[0]] above
            for key in rooms[room_index]:
                if key not in seen:
                    seen.add(key)
                    # stack.append(rooms[key])  # this works with stack = [rooms[0]] above
                    stack.append(key)
        return len(seen) == len(rooms)


# rooms is an adjacency list

rooms1 = [[1], [2], [3], []]
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
# Output: True

rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
# We can not enter room number 2 since the only key that unlocks it is in that room.
# Output: False

sol = Solution()
print(sol.canVisitAllRooms(rooms1))
print(sol.canVisitAllRooms_Iterative(rooms2))
