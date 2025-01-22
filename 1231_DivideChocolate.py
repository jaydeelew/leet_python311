# 1231. Divide Chocolate
# You have one chocolate bar that consists of some chunks.
# Each chunk has its own sweetness given by the array sweetness.
# You want to share the chocolate with your k friends so you start
# cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.
# Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
# Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.


class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        # check if this minimum level of sweetness can be maintained for all my friends and me
        def checkValidSweetnesses(mid):
            this_piece_sweetness = 0
            pieces = 0
            for s in sweetness:
                this_piece_sweetness += s
                if this_piece_sweetness >= mid:
                    pieces += 1
                    this_piece_sweetness = 0
            # can k + 1 or more pieces be produced with this minimum level of sweetness?
            return True if pieces >= k + 1 else False

        # no piece can be less sweet than the least sweetest chunk
        left = min(sweetness)
        # my piece (the smallest) cannot be sweeter than a piece from
        # the bar equally divided among my friends and me
        right = sum(sweetness) / (k + 1)

        # find and return the maximum sweetness
        while left <= right:
            mid = (left + right + 1) // 2
            if checkValidSweetnesses(mid):
                left = mid + 1
            else:
                right = mid - 1

        return int(right)


# sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 5
# # Output: 6

# sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4]
# k = 8
# # Output: 1

# sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
# k = 2
# # Output: 5

sweetness = [90670, 55382, 95298, 95795, 73204, 41464, 18675, 30104, 47442, 55307]
k = 6
# Output: 55382

sol = Solution()
print(sol.maximizeSweetness(sweetness, k))
