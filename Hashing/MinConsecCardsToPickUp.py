# 2260. Minimum Consecutive Cards to Pick Up
# Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate.
# If the array has no duplicates, return -1.

from collections import defaultdict


class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        # THIS VERSION STORES EVERY CARD INDEX IN card_positons DICTIONARY - O(n) EVERY RUN
        # card_positions = defaultdict(list)
        # shortest = float("inf")
        # for i in range(len(cards)):
        #     card_positions[cards[i]].append(i)  # when card appears, append its index to to it

        # shortest = float("inf")
        # for key in card_positions:
        #     index_list = card_positions[key]  # each card's list of indexes
        #     for i in range(len(index_list) - 1):  # length of 'index_list - 1' since next line accesses 'i + 1'
        #         sub_array_len = index_list[i + 1] - index_list[i] + 1  # since card indexes in order, results in subarray length
        #         shortest = min(shortest, sub_array_len)

        # THIS VERSION ONLY STORES INDEX IN card_positons DICTIONARY WHEN NEEDED - O(n) IN WORST CASE OF NO DUPLICATE CARDS
        card_positions = defaultdict(int)
        shortest = float("inf")
        for i in range(len(cards)):
            if cards[i] in card_positions:
                # (current card index) - (last index card was seen at) + 1
                shortest = min(shortest, i - card_positions[cards[i]] + 1)

            # update last index card was seen at
            card_positions[cards[i]] = i

        return shortest if shortest < float("inf") else -1  # type: ignore


cards = [1, 2, 7, 5, 2, 4]
# Output: 4

sol = Solution()
print(sol.minimumCardPickup(cards))
