# You are assigned to put some amount of boxes onto one truck.
# You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# - numberOfBoxesi is the number of boxes of type i.
# - numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda units: units[1], reverse=True)
        ans = 0

        for boxes, units in boxTypes:
            # if amount of boxes in this iteration is greater than current truckSize (remaining capacity)
            # reduce boxes to remaining capacity of truck (truckSize) by taking min of boxes & truckSize
            boxes = min(boxes, truckSize)
            ans += boxes * units
            truckSize -= boxes
            if truckSize == 0:
                break

        return ans


# boxTypes = [[1, 3], [2, 2], [3, 1]]
# truckSize = 4
# # Output: 8

boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
# Output: 91

sol = Solution()
print(sol.maximumUnits(boxTypes, truckSize))
